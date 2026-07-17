# while True:
#     edad = int(input("ingrese edad: "))
#     try:
#         edad == int()
#         print("edad valida")
#         break
#     except ValueError:
#         print("edad no valida, intente nuevamente")

# CORREGIDO
while True:
    try:
        edad = int(input("Ingrese edad: "))
        print(f"Edad valida: {edad}")
        break
    except ValueError:
        print("Debe ingresar una edad valida.")