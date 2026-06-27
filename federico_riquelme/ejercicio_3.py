## Problema 3: Programación funcional y listas de comprensión
##Dada la siguiente lista:
##palabras = ["hola", "mundo", "python"]

##Creá una nueva lista en una sola línea utilizando una **lista de comprensión**.

##La nueva lista debe contener las mismas palabras, pero convertidas completamente a mayúsculas mediante el método `.upper()`.

def formateador():
    palabras = ["hola", "mundo", "python"]
    palabras_mayusculas = [palabra.upper() for palabra in palabras]
    print(palabras_mayusculas)
formateador()