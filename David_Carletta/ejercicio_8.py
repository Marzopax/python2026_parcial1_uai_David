# CORREGIDO
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        
    def __str__(self):
        return f"{self.titulo} por {self.autor}"

libro = Libro("El Aleph", "Jorge Luis Borges")
print(libro)