
def pedir_entero():


        while True:
            try:
                entero = int(input("ingresa un entero: "))
                print(f"El número ingresado es: {entero}")
                break;
            except ValueError:
                print("Error: ingresa un número válido.")
pedir_entero()