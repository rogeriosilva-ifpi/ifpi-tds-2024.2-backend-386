from sqlmodel import SQLModel, Field


# class Clube(BaseModel):
class Clube(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  nome: str
  uf: str = Field(min_length=2, max_length=2)
  serie: str
  ano: int


class Jogadores(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  nome: str