from fastapi import APIRouter
from .models import *

router = APIRouter()


@router.get('/veiculos')
def veiculos_list():
  return ['Argo', 'Pálio']