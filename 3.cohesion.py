class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    def resumen(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, Cantidad páginas:{self.paginas}"
    

libro1 = Libro("Nuevo libro", "Nuevo autor", 500)


class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    def resumen(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, Cantidad páginas:{self.paginas}"

    #este método no debería pertenecer a la clase -> Carrito
    def agregar_al_carro(self):
        return f"Libro {self.titulo} agregado al carro"


libro1 = Libro("Nuevo libro", "Nuevo autor", 500)

print(libro1.agregar_al_carro())