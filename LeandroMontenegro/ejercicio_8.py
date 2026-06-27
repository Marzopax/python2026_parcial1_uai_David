class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    def __str__(self):
        return f"'{self.titulo}' por {self.autor}"

Libro1 = Libro("dasdasd", " dasdas García Márquez")
print(Libro1)