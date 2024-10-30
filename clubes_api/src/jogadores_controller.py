from fastapi import APIRouter


router = APIRouter()


@router.get('')
def jogadores_list():
  return []


@router.get('/{id}')
def jogadores_detail(id: int):
  return None


@router.post('')
def jogadores_create():
  return None