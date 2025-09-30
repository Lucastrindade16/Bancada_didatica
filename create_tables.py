# create_tables.py
from app.db.database import engine, Base
from app.db import models # Importa seus modelos

print("Conectando ao banco de dados e criando tabelas...")

# O comando mágico: cria todas as tabelas herdadas de Base
Base.metadata.create_all(bind=engine) 

print("✅ Tabelas criadas com sucesso (ou já existentes).")