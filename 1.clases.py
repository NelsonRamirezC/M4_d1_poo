class Animal:
    def __init__(self, nombre, raza, especie, disponible = True):
        self.nombre = nombre 
        self.raza = raza
        self.especie = especie
        self.disponible = disponible
    
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre}, estoy disponible para adopción"

perro_pepito = Animal("Pepito", "Pastor Alemán", "Perro", True)
gato_juanito = Animal("Juanito", "Pelo corto", "Gato", False)


print(perro_pepito.nombre)
print(gato_juanito.nombre)

perro_pepito.nombre = "Pepín"
print(perro_pepito.especie)

print(gato_juanito.saludar())

print(perro_pepito.disponible)
print(gato_juanito.disponible)

if(gato_juanito.disponible):
    print("disponible")
else:
    print("no disponible")


        
 


