class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor


    def mostrar_informacion(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
