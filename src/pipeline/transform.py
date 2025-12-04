from src.core import EntityMapper, get_english, TransformInterface
from src.domain.exceptions import TraducaoError

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
        self._process_flights()
        self._process_destinations()
        self._process_airlines()
        self._process_aircraftTypes()
        
    def _process_flights(self):
        dataframe_flights = pd.DataFrame(self.__raw_flights)
        dataframe_flights.to_csv('data/flights.csv')
    
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
                    raise TraducaoError(f"Coluna '{col}' não existe no dataframe")
            
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
                
        dataframe_destinations.to_csv('data/destinations.csv')
        return dataframe_destinations
        
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
                
        dataframe_airlines.to_csv('data/airlines.csv')
        return dataframe_airlines
            
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
                .astype(str)
                .str.strip()
            )
        
        for coluna in dataframe_aircraftTypes.columns:
            match coluna:
                case 'descricao_curta' | 'descricao_longa':
                    dataframe_aircraftTypes[coluna] = dataframe_aircraftTypes[coluna].str.title()
                case 'iata_principal' | 'iata_secundario':
                    dataframe_aircraftTypes[coluna] = dataframe_aircraftTypes[coluna].str.upper()
                case _:
                    pass
                
        dataframe_aircraftTypes.to_csv('data/aircraftTypes.csv')
        return dataframe_aircraftTypes
