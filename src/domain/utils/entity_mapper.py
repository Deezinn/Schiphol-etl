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
        dados = raw.get('flights')
        return [
            Flights(
            lastUpdatedAt=dado.get("lastUpdatedAt"),
            actualLandingTime=dado.get("actualLandingTime"),
            aircraftRegistration=dado.get("aircraftRegistration"),
            aircraftType=dado.get("aircraftType"),
            baggageClaim=dado.get("baggageClaim"),
            codeshares=dado.get("codeshares"),
            estimatedLandingTime=dado.get("estimatedLandingTime"),
            expectedTimeOnBelt=dado.get("expectedTimeOnBelt"),
            flightDirection=dado.get("flightDirection"),
            flightName=dado.get("flightName"),
            flightNumber=dado.get("flightNumber"),
            gate=dado.get("gate"),
            pier=dado.get("pier"),
            id=dado.get("id"),
            isOperationalFlight=dado.get("isOperationalFlight"),
            mainFlight=dado.get("mainFlight"),
            prefixIATA=dado.get("prefixIATA"),
            prefixICAO=dado.get("prefixICAO"),
            airlineCode=dado.get("airlineCode"),
            publicFlightState=dado.get("publicFlightState"),
            route=dado.get("route"),
            scheduleDateTime=dado.get("scheduleDateTime"),
            scheduleDate=dado.get("scheduleDate"),
            scheduleTime=dado.get("scheduleTime"),
            serviceType=dado.get("serviceType"),
            terminal=dado.get("terminal"),
            schemaVersion=dado.get("schemaVersion"),
            checkinAllocations=dado.get("checkinAllocations"),
            expectedSecurityFilter=dado.get("expectedSecurityFilter"),
        )
        for dado in dados
    ]