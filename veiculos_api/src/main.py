from fastapi import FastAPI

from .database import init_db
from .veiculos_controller import router

app = FastAPI()

app.include_router(router)

init_db()