from datetime import datetime, date
from sqlalchemy import (
    String,
    Integer,
    Boolean,
    DateTime,
    Date,
    Text,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Flight(Base):
    __tablename__ = "flights"

    id: Mapped[int] = mapped_column(primary_key=True)

    ultima_atualizacao: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False
    )

    hora_pouso_real: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False
    )

    hora_pouso_estimado: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False
    )

    tempo_previsto_esteira: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False
    )

    data_hora_programada: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False
    )

    data_programada: Mapped[date] = mapped_column(
        Date, nullable=False
    )

    hora_programada: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False
    )

    nome_voo: Mapped[str] = mapped_column(
        Text, nullable=False
    )

    numero_voo: Mapped[int] = mapped_column(
        Integer, nullable=False
    )

    voo_operacional: Mapped[bool] = mapped_column(
        Boolean, nullable=False
    )

    voo_principal: Mapped[str] = mapped_column(
        Text, nullable=False
    )

    prefixo_iata: Mapped[str] = mapped_column(
        String(2), nullable=False
    )

    prefixo_icao: Mapped[str] = mapped_column(
        String(3), nullable=False
    )

    codigo_companhia: Mapped[int] = mapped_column(
        Integer, nullable=False
    )

    registro_aeronave: Mapped[str] = mapped_column(
        String(10), nullable=False
    )

    tipo_aeronave: Mapped[dict] = mapped_column(
        JSONB, nullable=False
    )

    direcao_voo: Mapped[str] = mapped_column(
        String(1), nullable=False
    )

    estado_voo: Mapped[dict] = mapped_column(
        JSONB, nullable=False
    )

    portao: Mapped[str] = mapped_column(
        Text, nullable=False
    )

    pier: Mapped[str] = mapped_column(
        Text, nullable=False
    )

    terminal: Mapped[int] = mapped_column(
        Integer, nullable=False
    )

    retirada_bagagem: Mapped[dict] = mapped_column(
        JSONB, nullable=False
    )

    alocacao_checkin: Mapped[str] = mapped_column(
        Text, nullable=False
    )

    filtro_seguranca_previsto: Mapped[str] = mapped_column(
        Text, nullable=False
    )

    rota: Mapped[dict] = mapped_column(
        JSONB, nullable=False
    )

    codeshare: Mapped[dict] = mapped_column(
        JSONB, nullable=False
    )

    tipo_servico: Mapped[str] = mapped_column(
        String(1), nullable=False
    )

    versao_schema: Mapped[int] = mapped_column(
        Integer, nullable=False
    )
