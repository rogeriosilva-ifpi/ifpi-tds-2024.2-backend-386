from fastapi import FastAPI
from .clubes_controller import router as clubes_router
from .jogadores_controller import router as jogadores_router
from .database import init_db

# Rodar
# $ pip install -r requirements.txt
# $ fastapi dev src/main.py


app = FastAPI()

# Middlewares

# Controllers / Routers
app.include_router(clubes_router, prefix='/clubes')
app.include_router(jogadores_router, prefix='/jogadores')

# Inicializar DB
init_db()

