from fastapi import APIRouter, status, HTTPException
from .models import Clube
from sqlmodel import Session, select
from .database import get_engine


router = APIRouter()

# Instancia(objeto) de Clube
clubes = [
    Clube(id=1, nome='Santos', uf='SP', serie='B', ano=1900),
    Clube(id=2, nome='Fortaleza', uf='CE', serie='A', ano=1970),
    Clube(id=3, nome='Ceará', uf='CE', serie='B', ano=1958),
    Clube(id=4, nome='Palmeiras', uf='SP', serie='A', ano=1909)
  ]


@router.get('', status_code=status.HTTP_200_OK)
def clubes_list(uf: str | None = None, serie: str | None = None):
  session = Session(get_engine())
  sttm = select(Clube).where(Clube.uf == uf)
  clubes = session.exec(sttm).all()
  return clubes

 

@router.get('/{id}')
def clube_detail(id: int):
  for clube in clubes:
    if clube.id == id:
      return clube

  raise HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail='Clube não localizado!'
    )


@router.post('/', status_code=status.HTTP_201_CREATED)
def clubes_create(novo_clube: Clube):
  session = Session(get_engine())
  session.add(novo_clube)
  session.commit()
  session.refresh(novo_clube)
  return novo_clube


@router.put('/{id}')
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


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
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

# Utils
def obter_index_clube_por_id(id: int):
  for i in range(len(clubes)):
    if clubes[i].id == id:
      return i
    
  return None