from sqlmodel import SQLModel, create_engine

def get_engine():
  engine = create_engine('sqlite:///clubes.db')

  return engine


def init_db():
  SQLModel.metadata.create_all(get_engine())