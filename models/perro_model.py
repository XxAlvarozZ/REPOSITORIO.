class Perro:
    def __init__(self, id, nombre, raza, edad, tamaño):
        self.id = id
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.tamaño = tamaño

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "raza": self.raza,
            "edad": self.edad,
            "tamaño": self.tamaño
        }