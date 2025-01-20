from sqlmodel import SQLModel, create_engine
from decouple import config

def get_engine():
  engine = create_engine('sqlite:///veiculos.db')
  # postgresql://usuario:senha@endereco_host:port/nome_banco
  # Pegar os valores do .env
  # usuario = config('DB_USER')
  # senha = config('DB_PASS')
  # host = config('DB_HOST')
  # porta = config('DB_PORT')
  # nome = config('DB_NAME')
  # engine = create_engine(f'postgresql://{usuario}:{senha}@{host}:{porta}/{nome}')

  return engine


def init_db():
  # Cria as tabelas em BD para cada Classe SQLModel 
  SQLModel.metadata.create_all(get_engine())