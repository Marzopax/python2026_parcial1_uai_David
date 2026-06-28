class Libro:
    def __init__ (self, titulo, autor):
        self.titulo=titulo
        self.autor=autor
        
    def __str__(self):
        print (f'{self.titulo} por {self.autor}')
        
def main():
    libro = Libro(input("Ingrese el nombre del libro: ").title(),input("Ingrese el autor: ").title())
    libro.__str__()

if __name__=="__main__":
    main()