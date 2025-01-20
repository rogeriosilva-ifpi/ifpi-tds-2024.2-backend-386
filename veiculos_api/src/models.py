from sqlmodel import SQLModel, Field


class Veiculo(SQLModel, table=True):
  id: int = Field(default=None, primary_key=True)
  nome: str
  cor: str
  km: int
  valor: float
  ano: int