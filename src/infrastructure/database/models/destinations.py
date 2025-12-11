from pydantic import BaseModel, ConfigDict


class Destinations(BaseModel):
    pais: str
    codigo_iata: str
    nome_publico: str
    cidade: str
    
    model_config = ConfigDict(str_max_length=50)