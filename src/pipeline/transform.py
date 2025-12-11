from src.domain.interfaces import  TransformInterface
from src.domain.exceptions import TraducaoError
from src.domain.utils import safe_literal_eval, EntityMapper, get_english


from src.infrastructure.database import AircraftTypes, Airlines, Destinations

import pandas as pd

class Transform(TransformInterface):
    def __init__(self, raw_flights, raw_airlines, raw_destinations, aircraftTypes):
        self.__raw_flights = raw_flights
        self.__raw_airlines = raw_airlines
        self.__raw_destinations = raw_destinations
        self.__raw_aircraftTypes = aircraftTypes
    
    @classmethod
    def load_raw_data(cls, raw_data):
        if not raw_data:
            raise FileNotFoundError("Não consegui achar os dados de flights")
        
        if not isinstance(raw_data, dict):
            raise TypeError("Tipo dos dados deveriam vir como dict")
        
        return cls(
            raw_flights=EntityMapper.flights(raw_data.get('flights')),
            raw_airlines=EntityMapper.airlines(raw_data.get('airlines')),
            raw_destinations=EntityMapper.destinations(raw_data.get('destinations')),
            aircraftTypes=EntityMapper.aircraft_types(raw_data.get('aircraftTypes'))
        )
        
    def process_data(self):
        
        return { 'flights': self._process_flights(),
                'destinations': self._process_destinations(),
                'airlines': self._process_airlines(),
                'aircraftTypes': self._process_aircraftTypes()
        }
        
    def _process_flights(self):
        dataframe_flights = pd.DataFrame(self.__raw_flights)
        try:
            colunas_traduzidas = {
                "lastUpdatedAt": "ultima_atualizacao",
                "actualLandingTime": "hora_pouso_real",
                "aircraftRegistration": "registro_aeronave",
                "aircraftType": "tipo_aeronave",
                "baggageClaim": "retirada_bagagem",
                "codeshares": "codeshare",
                "estimatedLandingTime": "hora_pouso_estimado",
                "expectedTimeOnBelt": "tempo_previsto_esteira",
                "flightDirection": "direcao_voo",
                "flightName": "nome_voo",
                "flightNumber": "numero_voo",
                "gate": "portao",
                "pier": "pier",
                "id": "id",
                "isOperationalFlight": "voo_operacional",
                "mainFlight": "voo_principal",
                "prefixIATA": "prefixo_iata",
                "prefixICAO": "prefixo_icao",
                "airlineCode": "codigo_companhia",
                "publicFlightState": "estado_voo",
                "route": "rota",
                "scheduleDateTime": "data_hora_programada",
                "scheduleDate": "data_programada",
                "scheduleTime": "hora_programada",
                "serviceType": "tipo_servico",
                "terminal": "terminal",
                "schemaVersion": "versao_schema",
                "checkinAllocations": "alocacao_checkin",
                "expectedSecurityFilter": "filtro_seguranca_previsto"
            }
            
            for col in colunas_traduzidas.keys():
                if col not in dataframe_flights.columns:
                    raise TraducaoError(f"Coluna '{col}' não existe no dataframe.")
                
            dataframe_flights = dataframe_flights.rename(columns=colunas_traduzidas)
        except TraducaoError as e:
            pass
            # log de erro
        
            
        mapper_fillna = {
            'tipo_aeronave' : {'iataMain': "Não informado", 'iataSub': 'Não informado'},
            'retirada_bagagem': {'belts': 'Não informado'},
            'codeshare': {'codeshares': 'Não informado'},
            'estado_voo': {'flightStates': 'Não informado'},
            'rota': {'destomatopms': 'Não informado', 'eu': 'Não informado', 'visa': False}
        }
        
        sentinela = pd.Timestamp('1900-01-01', tz='UTC')
        
        valores_invalidos = ['N/A', 'null', 'na', 'undefined', None, 'NaN', 'NAN', 'nan', 'NONE']
                
        for col in dataframe_flights.columns:
             match col:
                case 'ultima_atualizacao' | 'hora_pouso_real' | 'hora_pouso_estimado' | \
                    'tempo_previsto_esteira' | 'data_hora_programada' | 'data_programada' | \
                    'hora_programada':
            
                    dataframe_flights[col] = pd.to_datetime(dataframe_flights[col], format='mixed')    
                    if col == 'data_programada':
                        dataframe_flights[col] = dataframe_flights[col].dt.strftime('%Y-%m-%d')

                    dataframe_flights[col] = dataframe_flights[col].fillna(sentinela)
                case 'registro_aeronave' | 'direcao_voo' | 'nome_voo' | 'prefixo_iata' | \
                    'prefixo_icao' | 'voo_principal' | 'pier' | 'portao' | 'tipo_servico' | \
                    'alocacao_checkin' | 'filtro_seguranca_previsto':
                    dataframe_flights[col] = dataframe_flights[col].astype(str).str.upper()
                    dataframe_flights[col] = dataframe_flights[col].replace(valores_invalidos, 'Não informado')
                    dataframe_flights[col] = dataframe_flights[col].fillna('Não informado')
                case 'tipo_aeronave' | 'retirada_bagagem' | 'codeshare' | 'estado_voo' | 'rota':
                    dataframe_flights[col] = dataframe_flights[col].apply(
                        lambda x: safe_literal_eval(x, mapper_fillna[col])
                    )
                case 'numero_voo' | 'codigo_companhia':
                    dataframe_flights[col] = pd.to_numeric(dataframe_flights[col], errors='coerce')
                    dataframe_flights[col] = dataframe_flights[col].fillna(0).astype('Int32')
                case 'id':
                    dataframe_flights[col] = pd.to_numeric(dataframe_flights[col], errors='coerce')
                    dataframe_flights[col] = dataframe_flights[col].fillna(0).astype('Int64')
                case 'versao_schema':
                    dataframe_flights[col] = pd.to_numeric(dataframe_flights[col], errors='coerce')
                    dataframe_flights[col] = dataframe_flights[col].fillna(0).astype('Int8')
                case 'voo_operacional':
                    dataframe_flights[col] = (
                        dataframe_flights[col]
                        .replace(valores_invalidos, False)
                        .astype('boolean')
                    )
                case 'terminal':
                    dataframe_flights[col] = pd.to_numeric(dataframe_flights[col], errors='coerce')
                    dataframe_flights[col] = dataframe_flights[col].fillna(0).astype('Int16')
                case _:
                    pass
                    
        print(dataframe_flights.to_dict(orient='records'))
        return dataframe_flights

    def _process_destinations(self):
        dataframe_destinations = pd.DataFrame(self.__raw_destinations) 
          
        try:
            colunas_traduzidas = {
                'country': 'pais',
                'iata': 'codigo_iata',
                'publicName': 'nome_publico',
                'city': 'cidade'
            }
            
            for col in colunas_traduzidas.keys():
                if col not in dataframe_destinations.columns:
                    raise TraducaoError(f"Coluna '{col}' não existe no dataframe.")
            
            dataframe_destinations = dataframe_destinations.rename(columns=colunas_traduzidas)
        except TraducaoError as e:
            print(f'error: não consegui traduzir as colunas {e}')
            # gerar log de erro
            
        valores_invalidos = ['N/A', 'null', 'none','NONE', 'na', 'undefined', '""', 'None']
        dataframe_destinations = dataframe_destinations.replace(valores_invalidos, 'Não informado').fillna('Não informado')
        
        for coluna in dataframe_destinations.columns:                
            match coluna:
                case 'pais' | 'cidade':
                    dataframe_destinations[coluna] = (
                        dataframe_destinations[coluna]
                        .str.title()
                        .str.strip()
                    )
                case 'codigo_iata':
                    dataframe_destinations[coluna] = (
                        dataframe_destinations[coluna]
                        .str.upper()
                        .str.strip()
                    )
                case 'nome_publico':
                    dataframe_destinations[coluna] = (
                        dataframe_destinations[coluna]
                        .apply(get_english)
                        .str.strip()
                    )
                case _:
                    pass
                
        return [Destinations(**row) for row in dataframe_destinations.to_dict(orient='records')]
        
    def _process_airlines(self):
        dataframe_airlines = pd.DataFrame(self.__raw_airlines)
    
        try: 
            colunas_traduzidas = {
                'iata': 'codigo_iata',
                'icao': 'codigo_icao',
                'nvls': 'nivel',
                'publicName': 'nome_publico'
            }
            
            for col in colunas_traduzidas.keys():
                if col not in dataframe_airlines.columns:
                    raise TraducaoError(f"Coluna '{col}' não existe no dataframe")
                
            dataframe_airlines = dataframe_airlines.rename(columns=colunas_traduzidas)
        except TraducaoError as e:
            print(f'error: não consegui traduzir as colunas {e}')
            # gerar log de erro
            
            
        valores_invalidos = ['N/A', 'null', 'none','NONE', 'na', 'undefined', '""', 'None']

        for coluna in dataframe_airlines.columns:
            match coluna:
                case 'nivel':
                    dataframe_airlines[coluna] = (
                        dataframe_airlines[coluna]
                        .replace(valores_invalidos, 0)
                        .astype('Int32')
                        .fillna(0)
                    )

                case 'codigo_iata' | 'codigo_icao':
                    dataframe_airlines[coluna] = (
                        dataframe_airlines[coluna]
                        .astype(str)
                        .str.upper()
                        .replace(valores_invalidos, 'Não informado')
                        .fillna('Não informado')
                        .str.strip()
                    )

                case 'nome_publico':
                    dataframe_airlines[coluna] = (
                        dataframe_airlines[coluna]
                        .astype(str)
                        .replace(valores_invalidos, 'Não informado')
                        .fillna('Não informado')
                        .str.title()
                        .str.strip()
                    )

                case _:
                    pass
                
        return [Airlines(**row) for row in dataframe_airlines.to_dict(orient='records')]
            
    def _process_aircraftTypes(self):
        dataframe_aircraftTypes = pd.DataFrame(self.__raw_aircraftTypes)
        try:
            colunas_traduzidas = {
                'iataMain': 'iata_principal', 
                'iataSub': 'iata_secundario', 
                'longDescription': 'descricao_longa', 
                'shortDescription': 'descricao_curta'
            }
            
            for col in colunas_traduzidas.keys():
                if col not in dataframe_aircraftTypes.columns:
                    raise TraducaoError(f"Coluna '{col}' não existe no dataframe")
                
            dataframe_aircraftTypes = dataframe_aircraftTypes.rename(columns=colunas_traduzidas)
        except TraducaoError as e:
            print(f'error: não consegui traduzir as colunas {e}')
            # gerar log de erro

        valores_invalidos = ['N/A', 'null', 'none','NONE', 'na', 'undefined', '""', 'None']
        
        for coluna in dataframe_aircraftTypes.columns:
            dataframe_aircraftTypes[coluna] = (
                dataframe_aircraftTypes[coluna]
                .replace(valores_invalidos, 'Não informado')
                .fillna('Não informado')
                .str.strip()
                .astype(str)
            )
        
        for coluna in dataframe_aircraftTypes.columns:
            match coluna:
                case 'descricao_curta' | 'descricao_longa':
                    dataframe_aircraftTypes[coluna] = dataframe_aircraftTypes[coluna].str.title()
                case 'iata_principal' | 'iata_secundario':
                    dataframe_aircraftTypes[coluna] = dataframe_aircraftTypes[coluna].str.upper()
                case _:
                    pass
                             
        return [AircraftTypes(**row) for row in dataframe_aircraftTypes.to_dict(orient='records')]
