from fastapi import FastAPI
from apis.perros_api import router as perros_router

app = FastAPI(
    title="Sistema de Gestión para Albergue de Perros",
    description="CRUD completo conectado a MySQL sin ORM (solo mysql.connector)",
    version="1.0.0"
)

app.include_router(perros_router)

@app.get("/")
def root():
    return {"mensaje": "Bienvenido al Sistema del Albergue de Perros 🐕"}