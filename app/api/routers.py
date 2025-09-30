from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db import models, schemas
from app.db.database import get_db

router = APIRouter()

@router.get(
    "/producao",
    response_model=List[schemas.DadosProducao],
    tags=["Produção"],
    summary="Consulta os últimos registros de produção",
    description="Retorna uma lista dos últimos 100 registros de dados de produção."
)
def read_dados_producao(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    dados = db.query(models.DadosProducao).offset(skip).limit(limit).all()
    return dados

@router.get(
    "/estoque",
    response_model=List[schemas.DadosEstoque],
    tags=["Estoque"],
    summary="Consulta os últimos registros de estoque",
    description="Retorna uma lista dos últimos 100 registros de dados de estoque."
)
def read_dados_estoque(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    dados = db.query(models.DadosEstoque).offset(skip).limit(limit).all()
    return dados

@router.get(
    "/ambiente",
    response_model=List[schemas.DadosAmbientais],
    tags=["Dados Ambientais"],
    summary="Consulta os últimos registros de dados ambientais",
    description="Retorna uma lista dos últimos 100 registros de temperatura e umidade."
)
def read_dados_ambientais(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    dados = db.query(models.DadosAmbientais).offset(skip).limit(limit).all()
    return dados