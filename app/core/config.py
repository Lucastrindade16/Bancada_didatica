import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Banco de Dados
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    # MQTT
    MQTT_BROKER_HOST = os.getenv("MQTT_BROKER_HOST")
    MQTT_BROKER_PORT = int(os.getenv("MQTT_BROKER_PORT", 1883))
    MQTT_CLIENT_ID = os.getenv("MQTT_CLIENT_ID")
    MQTT_TOPIC_PRODUCAO = os.getenv("MQTT_TOPIC_PRODUCAO")
    MQTT_TOPIC_ESTOQUE = os.getenv("MQTT_TOPIC_ESTOQUE")
    MQTT_TOPIC_AMBIENTE = os.getenv("MQTT_TOPIC_AMBIENTE")

settings = Settings()