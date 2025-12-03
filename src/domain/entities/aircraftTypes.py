from dataclasses import dataclass

@dataclass
class AircraftTypes:
    iataMain: str
    iataSub: str
    longDescription: str
    shortDescription: str