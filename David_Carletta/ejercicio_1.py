def llamarse(nombre, apellido):
    nombre = str(input("ingrese nombre: ")).strip().capitalize()
    apellido = str(input("ingrese apellido: ")).strip().capitalize()
    print("Hola, " + nombre + " " + apellido)
    return nombre, apellido

llamarse("", "")