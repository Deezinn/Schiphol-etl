from .base import Base

from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

class Destinations(Base):
    __tablename__ = 'destinations'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    pais: Mapped[str] = mapped_column(String(50), nullable=False)
    codigo_iata: Mapped[str] = mapped_column(String(50), nullable=False)
    nome_publico: Mapped[str] = mapped_column(String(50), nullable=False)
    cidade: Mapped[str] = mapped_column(String(50), nullable=False) 