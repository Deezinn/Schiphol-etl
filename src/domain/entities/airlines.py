from dataclasses import dataclass

@dataclass
class Airlines:
    iata: str
    icao: str
    nvls: int
    publicName: str