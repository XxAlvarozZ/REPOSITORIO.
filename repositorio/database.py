import mysql.connector

def obtener_conexion():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",              # Cambia por tu usuario MySQL
        password="tu_contraseña", # Cambia por tu contraseña
        database="albergue"       # Nombre de tu base de datos
    )
    return conexion