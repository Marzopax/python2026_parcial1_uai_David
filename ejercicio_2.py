def pedir_entero():
    while True:
        try:
            edad = input("Ingrese su edad: ")
            edad_entera = int(edad)
            print(f"Edad registrada: {edad_entera}")
            return edad_entera
        except ValueError:
            print("Debe ingresar un número válido.")
pedir_entero()
