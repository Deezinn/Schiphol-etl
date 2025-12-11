from datetime import datetime

from pydantic import BaseModel, ConfigDict


class Flights(BaseModel):
    ultima_atualizacao: datetime
    hora_pouso_real: datetime
    registro_aeronave: str
    tipo_aeronave: dict[str, str]
    retirada_bagagem: dict[str, list[str]]
    codeshare: dict[str, list[str]]
    hora_pouso_estimado: datetime
    tempo_previsto_esteira: datetime
    direcao_voo: str
    nome_voo: str
    numero_voo: int
    portao: str
    pier: str
    id: int
    voo_operacional: bool
    voo_principal: str
    prefixo_iata: str
    prefixo_icao: str
    codigo_companhia: int
    estado_voo: dict[str, list[str]]
    rota: dict[str, list[str] | bool | str]
    data_hora_programada: datetime
    data_programada: str
    hora_programada: datetime
    tipo_servico: str
    terminal: int
    versao_schema: int
    alocacao_checkin: str
    filtro_seguranca_previsto: str
    

    
    
    



