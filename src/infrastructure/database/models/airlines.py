from .base import Base

from sqlalchemy.types import String, Integer
from sqlalchemy.orm import mapped_column, Mapped

class Airlines(Base):
    __tablename__ = 'airlines'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    codigo_iata: Mapped[str] = mapped_column(String(50), nullable=False)
    codigo_icao: Mapped[str] = mapped_column(String(50), nullable=False)
    nivel: Mapped[int] = mapped_column(Integer, nullable=False)
    nome_publico: Mapped[str] = mapped_column(String(50), nullable=False) 