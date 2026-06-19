def pedir_entero():
    while True:
        try:
            entrada = input("Ingrese su edad: ")
            edad = int(entrada)
            print(f"Edad registrada: {edad}")
            return edad
        except ValueError:
            print("Debe ingresar un número válido.")

pedir_entero()