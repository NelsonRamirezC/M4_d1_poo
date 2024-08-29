class Perro():
    def hablar(self):
        print("Gauf")
        
        
class Gato():
    def hablar(self):
        print("Meow")
        
class Canario():
    def hablar(self):
        print("peow poew")
        
perro = Perro()
gato = Gato()
canario = Canario()


animales = [perro, gato, canario]

for animal in animales:
    animal.hablar()