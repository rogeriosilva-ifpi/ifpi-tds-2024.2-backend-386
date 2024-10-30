from pydantic import BaseModel, Field


class Clube(BaseModel):
  id: int | None = None
  nome: str
  uf: str = Field(min_length=2, max_length=2)
  serie: str
  ano: int


class Jogadores(BaseModel):
  id: int | None = None
  nome: str