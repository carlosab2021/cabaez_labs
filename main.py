from fastapi import FastAPI
from app.app_porcentaje import app_porcentaje
from app.app_genero import app_genero
from app.app_genero_horas import app_genero_horas
from app.app_desarrollador import app_desarrollador
from app.app_userdata import app_userdata

app = FastAPI()

# Registra las rutas para cada aplicación
app.include_router(app_porcentaje, prefix="/porcentaje", tags=["porcentaje"])
app.include_router(app_genero, prefix="/genero", tags=["genero"])
app.include_router(app_genero_horas, prefix="/genero_horas", tags=["genero_horas"])
app.include_router(app_desarrollador, prefix="/desarrollador", tags=["desarrollador"])
app.include_router(app_userdata, prefix="/user_data", tags=["user_data"])
