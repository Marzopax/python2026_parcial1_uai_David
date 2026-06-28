
def pedir_entero():
    while True:
        try:
            edad = int(input("Ingresá tu edad: "))
            return edad
        except ValueError:
            print("Error: debés ingresar un número entero.")


edad = pedir_entero()
print(f"Tu edad es {edad} años.")