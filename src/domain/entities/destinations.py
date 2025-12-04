from dataclasses import dataclass

@dataclass
class Destinations:
    city: str
    country: str
    iata: str
    publicName: str