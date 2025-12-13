from pydantic import BaseModel, ConfigDict


class AircraftTypes(BaseModel):
    iata_principal: str
    iata_secundario: str
    descricao_longa: str
    descricao_curta: str 

    model_config = ConfigDict(str_max_length=50)