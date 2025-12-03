from dataclasses import dataclass

@dataclass
class Airlines:
    codigo_iata: str
    codigo_icao: str
    nivel: int
    nome_publico: str