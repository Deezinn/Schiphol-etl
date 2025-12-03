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
            Airlines(iata=dado.get('iata'),
                     icao=dado.get('icao'),
                     nvls=dado.get('nvls'),
                     publicName=dado.get('publicName'))
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
        # lastUpdatedAt,
        # actualLandingTime,
        # aircraftRegistration,
        # aircraftType,
        # baggageClaim,
        # codeshares,
        # estimatedLandingTime,
        # expectedTimeOnBelt,
        # flightDirection,
        # flightName,
        # flightNumber,
        # gate,
        # pier,
        # id,
        # isOperationalFlight,
        # mainFlight,
        # prefixIATA,
        # prefixICAO,
        # airlineCode,
        # publicFlightState,
        # route,
        # scheduleDateTime,
        # scheduleDate,
        # scheduleTime,
        # serviceType,
        # terminal,
        # schemaVersion,
        # actualOffBlockTime,
        # checkinAllocations,
        # expectedSecurityFilter
        
        return raw