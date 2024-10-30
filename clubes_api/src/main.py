from fastapi import FastAPI
from .clubes_controller import router as clubes_router
from .jogadores_controller import router as jogadores_router


app = FastAPI()

# Middlewares


# Controllers / Routers
app.include_router(clubes_router, prefix='/clubes')
app.include_router(jogadores_router, prefix='/jogadores')

