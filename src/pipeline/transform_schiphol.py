import pandas as pd
from ..utils import get_english
from ..core import BaseTransform

class TransformSchiphol(BaseTransform):
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

        return cls(raw_flights=raw_data.get('flights') , raw_airlines=raw_data.get('airlines'),
            raw_destinations=raw_data.get('destinations'), aircraftTypes=raw_data.get('aircraftTypes'))
        
    def process_data(self):
        self._process_flights()
        self._process_destinations()
        self._process_airlines()
        self._process_aircraftTypes()
        
    def _process_flights(self):
        dataframe_flights = pd.DataFrame(self.__raw_flights['flights'])
        dataframe_flights.to_csv('data/flights.csv')
    
    def _process_destinations(self):
        new_column_name = {
            'country': 'pais',
            'iata': 'codigo_iata',
            'publicName': 'nome_publico',
            'city': 'cidade'
        }

        dataframe_destinations = pd.DataFrame(self.__raw_destinations['destinations'])   
        dataframe_destinations = dataframe_destinations.rename(columns=new_column_name)
        
        for coluna in dataframe_destinations.columns:
            match coluna:
                case 'pais' | 'cidade':
                    dataframe_destinations[coluna] = dataframe_destinations[coluna].str.title()
                    dataframe_destinations[coluna] = dataframe_destinations[coluna].str.strip()
                    dataframe_destinations[coluna] = dataframe_destinations[coluna].fillna('Não informado')
                case 'codigo_iata':
                    dataframe_destinations[coluna] = dataframe_destinations[coluna].str.upper()
                    dataframe_destinations[coluna] = dataframe_destinations[coluna].str.strip()
                    dataframe_destinations[coluna] = dataframe_destinations[coluna].fillna('Não informado')
                case 'nome_publico':
                    dataframe_destinations[coluna] = dataframe_destinations[coluna].apply(get_english)
                    dataframe_destinations[coluna] = dataframe_destinations[coluna].str.strip()
                    dataframe_destinations[coluna] = dataframe_destinations[coluna].fillna('Não informado')
                case _:
                    print(f"Coluna inválida: {coluna}")
        dataframe_destinations.to_csv('data/destinations.csv')
        return dataframe_destinations
        
    def _process_airlines(self):
        dataframe_airlines = pd.DataFrame(self.__raw_airlines['airlines'])
        dataframe_airlines.to_csv('data/airlines.csv')
    
    def _process_aircraftTypes(self):
        dataframe_aircraftTypes = pd.DataFrame(self.__raw_aircraftTypes['aircraftTypes'])
        dataframe_aircraftTypes.to_csv('data/aircraftTypes.csv')    
        
        
         