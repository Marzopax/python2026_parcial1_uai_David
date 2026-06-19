def pedir_entero():
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            print(f"Edad registrada: {edad}")
            break
        except ValueError:
            print("Debe ingresar un número válido.")

pedir_entero()
