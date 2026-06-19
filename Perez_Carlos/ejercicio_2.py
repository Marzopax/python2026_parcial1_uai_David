def pedir_entero():
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            break
        except ValueError:
            print("Debe ingresar un número válido.")

print(f"Edad registrada: {edad}")
