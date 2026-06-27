## Problema 8: Programación Orientada a Objetos
##Definí una clase llamada `Libro`.
##La clase debe:

##Tener un método constructor `__init__`.
##Recibir y asignar los atributos `titulo` y `autor`.
##Implementar el método especial `__str__`.
##Permitir que, al imprimir un objeto con `print()`, se muestre una cadena con el siguiente formato:

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    def __str__(self):
        return f"{self.titulo} por {self.autor}"
mi_libro = Libro("El Quijote", "Miguel de Cervantes")
print(mi_libro) 
