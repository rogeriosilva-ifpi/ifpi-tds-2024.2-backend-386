from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Clube(BaseModel):
  id: int | None = None
  nome: str
  uf: str
  serie: str
  ano: int

# Instancia(objeto) de Clube
clubes = [
    Clube(id=1, nome='Santos', uf='SP', serie='B', ano=1900),
    Clube(id=2, nome='Fortaleza', uf='CE', serie='A', ano=1970)
  ]


@app.get('/clubes', status_code=status.HTTP_200_OK)
def clubes_list():
  return clubes


@app.get('/clubes/{id}')
def clube_detail(id: int):
  for clube in clubes:
    if clube.id == id:
      return clube

  raise HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail='Clube não localizado!'
    )


@app.post('/clubes', status_code=status.HTTP_201_CREATED)
def clubes_create(novo_clube: Clube):
  clubes.append(novo_clube)
  return novo_clube


@app.put('/clubes/{id}')
def clube_edit(id: int, clube_editado: Clube):
  index = obter_index_clube_por_id(id)

  if index != None:
    clubes[index] = clube_editado
    return
  else:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail='Clube não localizado!'
    )


@app.delete('/clubes/{id}', status_code=status.HTTP_204_NO_CONTENT)
def clube_remove(id: int):
  index = obter_index_clube_por_id(id)

  if index != None:
    clubes.pop(index)
    return
  else:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail='Clube não localizado!'
    )


def obter_index_clube_por_id(id: int):
  for i in range(len(clubes)):
    if clubes[i].id == id:
      return i
    
  return None