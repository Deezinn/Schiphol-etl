from src.domain import Flights, AircraftTypes, Airlines, Destinations

class EntityMapper:
    
    @staticmethod
    def aircraft_types(raw):
        dados = raw.get('aircraftTypes')
        return ([
            AircraftTypes(iataMain=dado.get("iataMain"),
                          iataSub=dado.get("iataSub"),
                          longDescription=dado.get('longDescription'),
                          shortDescription=dado.get('shortDescription'))
         for dado in dados ])
    
    @staticmethod
    def airlines(raw):
        # 'iata', 'icao', 'nvls', 'publicName'
        dados = raw.get('airlines')
        return ([
            Airlines(codigo_iata=dado.get('iata'),
                     codigo_icao=dado.get('icao'),
                     nivel=dado.get('nvls'),
                     nome_publico=dado.get('publicName'))
        for dado in dados])
    
    @staticmethod
    def destinations(raw):
        dados = raw.get('destinations')
        return ([
            Destinations(city=dado.get('city'),
                         country=dado.get('country'),
                         iata=dado.get('iata'),
                         publicName=dado.get('publicName'))
            for dado in dados])

    @staticmethod
    def flights(raw):
        return raw