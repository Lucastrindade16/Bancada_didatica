import paho.mqtt.client as mqtt
import json
from app.db.database import SessionLocal
from app.db import models, schemas
from app.core.config import settings
from pydantic import ValidationError

def persist_data(db, data_model, db_model):
    """Função genérica para persistir dados no banco."""
    db_data = db_model(**data_model.model_dump())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    print(f"Dados salvos: {db_data.id}")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado ao MQTT Broker com sucesso!")
        # Inscreve-se nos tópicos de interesse
        client.subscribe(settings.MQTT_TOPIC_PRODUCAO)
        client.subscribe(settings.MQTT_TOPIC_ESTOQUE)
        client.subscribe(settings.MQTT_TOPIC_AMBIENTE)
        print(f"Inscrito nos tópicos: {settings.MQTT_TOPIC_PRODUCAO}, {settings.MQTT_TOPIC_ESTOQUE}, {settings.MQTT_TOPIC_AMBIENTE}")
    else:
        print(f"Falha na conexão, código de retorno: {rc}\n")

def on_message(client, userdata, msg):
    print(f"Mensagem recebida no tópico {msg.topic}")
    db = SessionLocal()
    try:
        payload = json.loads(msg.payload.decode())
        
        if msg.topic == settings.MQTT_TOPIC_PRODUCAO:
            data_model = schemas.DadosProducaoCreate(**payload)
            persist_data(db, data_model, models.DadosProducao)
            
        elif msg.topic == settings.MQTT_TOPIC_ESTOQUE:
            data_model = schemas.DadosEstoqueCreate(**payload)
            persist_data(db, data_model, models.DadosEstoque)

        elif msg.topic == settings.MQTT_TOPIC_AMBIENTE:
            data_model = schemas.DadosAmbientaisCreate(**payload)
            persist_data(db, data_model, models.DadosAmbientais)

    except json.JSONDecodeError:
        print("Erro: A mensagem não é um JSON válido.")
    except ValidationError as e:
        print(f"Erro de validação Pydantic: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    finally:
        db.close()

def run_consumer():
    client = mqtt.Client(client_id=settings.MQTT_CLIENT_ID)
    client.on_connect = on_connect
    client.on_message = on_message
    
    client.connect(settings.MQTT_BROKER_HOST, settings.MQTT_BROKER_PORT, 60)
    
    # Loop para manter o cliente rodando e processando mensagens
    client.loop_forever()