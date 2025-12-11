from pydantic import BaseModel, ConfigDict


class Airlines(BaseModel):
    codigo_iata: str
    codigo_icao: str
    nivel: int
    nome_publico: str
    
    model_config = ConfigDict(str_max_length=50)