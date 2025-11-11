from repositorio import perros_repo

def registrar_perro(nombre, raza, edad, tamaño):
    return perros_repo.guardar_perro(nombre, raza, edad, tamaño)

def listar_perros():
    return perros_repo.obtener_todos()

def obtener_perro(id):
    return perros_repo.obtener_por_id(id)

def editar_perro(id, nombre, raza, edad, tamaño):
    perro_existente = perros_repo.obtener_por_id(id)
    if perro_existente:
        return perros_repo.actualizar_perro(id, nombre, raza, edad, tamaño)
    return {"error": "Perro no encontrado"}

def eliminar_perro(id):
    perro_existente = perros_repo.obtener_por_id(id)
    if perro_existente:
        return perros_repo.eliminar_perro(id)
    return {"error": "Perro no encontrado"}