from pydantic import BaseModel, Field
from datetime import datetime

# Schema para Dados Ambientais
class DadosAmbientaisBase(BaseModel):
    temperatura: float = Field(..., gt=0, description="Temperatura em graus Celsius")
    umidade: float = Field(..., ge=0, le=100, description="Umidade relativa do ar (%)")

class DadosAmbientaisCreate(DadosAmbientaisBase):
    pass

class DadosAmbientais(DadosAmbientaisBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True

# Schema para Dados de Produção
class DadosProducaoBase(BaseModel):
    pecas_produzidas: int = Field(..., ge=0)
    pecas_rejeitadas: int = Field(..., ge=0)

class DadosProducaoCreate(DadosProducaoBase):
    pass

class DadosProducao(DadosProducaoBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True
        
# Schema para Dados de Estoque
class DadosEstoqueBase(BaseModel):
    item_id: str = Field(..., min_length=1, max_length=50)
    quantidade: int = Field(..., ge=0)

class DadosEstoqueCreate(DadosEstoqueBase):
    pass

class DadosEstoque(DadosEstoqueBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True