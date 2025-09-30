from sqlalchemy import Column, Integer, String, Float, DateTime, func
from .database import Base

class DadosProducao(Base):
    __tablename__ = "dados_producao"
    id = Column(Integer, primary_key=True, index=True)
    pecas_produzidas = Column(Integer, nullable=False)
    pecas_rejeitadas = Column(Integer, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

class DadosEstoque(Base):
    __tablename__ = "dados_estoque"
    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(String(50), nullable=False)
    quantidade = Column(Integer, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

class DadosAmbientais(Base):
    __tablename__ = "dados_ambientais"
    id = Column(Integer, primary_key=True, index=True)
    temperatura = Column(Float, nullable=False)
    umidade = Column(Float, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())