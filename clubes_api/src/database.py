from sqlmodel import SQLModel, create_engine

def get_engine():
  # engine = create_engine('sqlite:///base_clubes.db')
                        # postgresql://usuario:senha@endereco_host:port/nome_banco
  engine = create_engine('postgresql://postgres:postgres@localhost:5432/clubes_386')

  return engine


def init_db():
  # Cria as tabelas em BD para cada Classe SQLModel 
  SQLModel.metadata.create_all(get_engine())