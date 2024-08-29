class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre}"
    
class Perro(Animal):
    def __init__(self, nombre, pelaje):
        super().__init__(nombre)
        self.pelaje = pelaje
        
    def saludar(self):
        return f"Ey, estoy disponible"


class Canario(Animal):
    def __init__(self, nombre, plumaje):
        super().__init__(nombre)
        self.plumaje = plumaje
        

pepito = Perro("Pepito", "Corto")

print(pepito.saludar())


piolin = Canario("Piolín", "Largo")

print(piolin.plumaje)

