from fastapi import FastAPI
from app.api import routers

# Customização da documentação Swagger / OpenAPI
app = FastAPI(
    title="API da Bancada Didática 4.0 - Camila",
    description="Esta API provê acesso aos dados coletados via MQTT pela bancada didática, incluindo informações de produção, estoque e sensores ambientais.",
    version="1.0.0",
    contact={
        "name": "Equipe de Desenvolvimento",
        "email": "dev@exemplo.com",
    },
)

app.include_router(routers.router, prefix="/api/v1")

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Bem-vindo à API da Bancada Didática Camila. Acesse /docs para a documentação."}