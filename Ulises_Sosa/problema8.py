class Libro:
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor
    
    def __str__(self):
        return f"{self.titulo} de {self.autor}"
    
def main():
    libro1 = Libro("Dragon ball z", "Toriyama")
    print(libro1)

main()