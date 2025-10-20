# Passo a Passo:
  - Primeiro você criara uma pasta com o nome desejado (por exemplo: Bancada_Didatica), logo depois abra ela no VSC e crie um ambiente virtual venv como o seguinte comando no terminal: python -m venv .venv, isto serve pra isolar as dependências de cada projeto Python, evitando conflitos de bibliotecas e versões entre diferentes projetos.
  - Depois execute o comando: pip freeze > requirements.txt, e logo após: pip install -r requirements.txt. Onde vai servir para listar as bibliotecas e suas versões 
  
  - Você precisara fazer instalações pelo terminal do Visual Studio Code, elas seram:
    -pip install uvicorn (para instalar um servidor web uvicorn para aplicações assíncronas, como fastApi)
    -pip install fastapi "uvicorn[standard]" (instala o framework web FastAPI e também o servidor Uvicorn na versão com dependências [standard], que inclui ferramentas úteis para desenvolvimento, permitindo que você crie e rode aplicações web)
