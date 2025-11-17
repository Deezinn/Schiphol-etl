import pandas as pd

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
        self._to_csv()
        
    def _to_csv(self):
        pd.DataFrame(self.__raw_flights['flights']).to_csv('data/flights.csv')
        pd.DataFrame(self.__raw_airlines['airlines']).to_csv('data/airlines.csv')
        pd.DataFrame(self.__raw_destinations['destinations']).to_csv('data/destinations.csv')
        pd.DataFrame(self.__raw_aircraftTypes['aircraftTypes']).to_csv('data/aircraftTypes.csv')
        
        
         