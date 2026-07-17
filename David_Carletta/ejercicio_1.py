# def llamarse(nombre, apellido):
#     nombre = str(input("ingrese nombre: ")).strip().capitalize()
#     apellido = str(input("ingrese apellido: ")).strip().capitalize()
#     print("Hola, " + nombre + " " + apellido)
#     return nombre, apellido

# llamarse("", "")

# CORREGIDO
def saludar_usuario():
    nombre = input("Ingrese su nombre: ")
    nombre_formateado = nombre.strip().title()
    print(f"Hola, {nombre_formateado}")

saludar_usuario()