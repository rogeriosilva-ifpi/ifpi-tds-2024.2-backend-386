from fastapi import APIRouter, status, HTTPException
from .models import Clube
from sqlmodel import Session, select
from .database import get_engine


router = APIRouter()


@router.get('', status_code=status.HTTP_200_OK)
def clubes_list(uf: str | None = None, serie: str | None = None):
  session = Session(get_engine())
  
  statement = select(Clube)

  if uf:
    statement = statement.where(Clube.uf == uf)

  if serie:
    statement = statement.where(Clube.serie == serie)
  
  clubes = session.exec(statement).all()
  return clubes


@router.get('/{id}')
def clube_detail(id: int):
  with Session(get_engine()) as session:
    try:
      return get_clube_by_id(id, session)
    except:
      raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Clube não localizado!'
        )


@router.post('', status_code=status.HTTP_201_CREATED)
def clubes_create(novo_clube: Clube):
  session = Session(get_engine())
  session.add(novo_clube)
  session.commit()
  session.refresh(novo_clube)
  return novo_clube


@router.put('/{id}')
def clube_edit(id: int, clube_editado: Clube):
    with Session(get_engine()) as session:
      try:
        clube = get_clube_by_id(id, session)
        clube.nome = clube_editado.nome
        clube.serie = clube_editado.serie
        clube.ano = clube_editado.ano
        clube.uf = clube_editado.uf

        session.add(clube)
        session.commit()
        session.refresh(clube)
        return clube
      except:
        raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND,
          detail='Clube não localizado!'
        )


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def clube_remove(id: int):
  with Session(get_engine()) as session:
    try:
      clube = get_clube_by_id(id, session)
      session.delete(clube)
      session.commit()
      return
    except:
      raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Clube não localizado!'
      )


def get_clube_by_id(id: int, session: Session):
  statement = select(Clube).where(Clube.id == id)
  clube = session.exec(statement).one()
  return clube
