from fastapi import APIRouter
from servicio import perros_servicio

router = APIRouter(prefix="/perros", tags=["Perros"])

@router.post("/")
def crear_perro(nombre: str, raza: str, edad: int, tamaño: str):
    return perros_servicio.registrar_perro(nombre, raza, edad, tamaño)

@router.get("/")
def obtener_perros():
    return perros_servicio.listar_perros()

@router.get("/{id}")
def obtener_perro(id: int):
    return perros_servicio.obtener_perro(id)

@router.put("/{id}")
def actualizar_perro(id: int, nombre: str, raza: str, edad: int, tamaño: str):
    return perros_servicio.editar_perro(id, nombre, raza, edad, tamaño)

@router.delete("/{id}")
def eliminar_perro(id: int):
    return perros_servicio.eliminar_perro(id)