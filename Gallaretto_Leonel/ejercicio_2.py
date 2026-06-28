
def main():
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            if 100 > edad > 0:
                print(f"Edad registrada: {edad}")
                break
            else:
                print("Debe ingresar una edad entre 1 y 99.")
        except ValueError:
            print("Debe ingresar un número válido.")
main()