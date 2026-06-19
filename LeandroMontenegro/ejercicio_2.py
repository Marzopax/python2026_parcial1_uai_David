
def pedir_entero():


        while True:
            try:
                entero = int(input("ingresa edad: "))
                print(f"la edad ingresada es: {entero}")
                break;
            except ValueError:
                print("Error: ingresa un número válido.")
pedir_entero()