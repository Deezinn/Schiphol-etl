from dataclasses import dataclass
from typing import Optional, Any, Dict, List

@dataclass
class Flights:
    lastUpdatedAt: Optional[str] = None
    actualLandingTime: Optional[str] = None
    aircraftRegistration: Optional[str] = None
    aircraftType: Optional[str] = None
    baggageClaim: Optional[Dict[str, Any]] = None
    codeshares: Optional[List[str]] = None
    estimatedLandingTime: Optional[str] = None
    expectedTimeOnBelt: Optional[str] = None
    flightDirection: Optional[str] = None
    flightName: Optional[str] = None
    flightNumber: Optional[str] = None
    gate: Optional[str] = None
    pier: Optional[str] = None
    id: Optional[int] = None
    isOperationalFlight: Optional[bool] = None
    mainFlight: Optional[bool] = None
    prefixIATA: Optional[str] = None
    prefixICAO: Optional[str] = None
    airlineCode: Optional[str] = None
    publicFlightState: Optional[Dict[str, Any]] = None
    route: Optional[Dict[str, Any]] = None
    scheduleDateTime: Optional[str] = None
    scheduleDate: Optional[str] = None
    scheduleTime: Optional[str] = None
    serviceType: Optional[str] = None
    terminal: Optional[str] = None
    schemaVersion: Optional[int] = None
    checkinAllocations: Optional[List[Dict[str, Any]]] = None
    expectedSecurityFilter: Optional[str] = None