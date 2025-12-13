from .base import Base

from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

class AircraftTypes(Base):
    __tablename__ = 'aircraft_types'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    iata_principal: Mapped[str] = mapped_column(String(50), nullable=False)
    iata_secundario: Mapped[str] = mapped_column(String(50), nullable=False)
    descricao_longa: Mapped[str] = mapped_column(String(50), nullable=False)
    descricao_curta: Mapped[str] = mapped_column(String(50), nullable=False) 