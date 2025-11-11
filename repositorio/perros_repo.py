from repositorio.database import obtener_conexion
from models.perro_model import Perro

def guardar_perro(nombre, raza, edad, tamaño):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "INSERT INTO perros (nombre, raza, edad, tamaño) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (nombre, raza, edad, tamaño))
    conexion.commit()
    conexion.close()
    return {"mensaje": "Perro registrado correctamente"}

def obtener_todos():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM perros")
    resultados = cursor.fetchall()
    conexion.close()
    return resultados

def obtener_por_id(id):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM perros WHERE id = %s", (id,))
    resultado = cursor.fetchone()
    conexion.close()
    return resultado

def actualizar_perro(id, nombre, raza, edad, tamaño):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "UPDATE perros SET nombre=%s, raza=%s, edad=%s, tamaño=%s WHERE id=%s"
    cursor.execute(sql, (nombre, raza, edad, tamaño, id))
    conexion.commit()
    conexion.close()
    return {"mensaje": "Perro actualizado correctamente"}

def eliminar_perro(id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM perros WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()
    return {"mensaje": "Perro eliminado correctamente"}