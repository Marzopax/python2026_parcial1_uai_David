def pedir_entero():
    while True:
        try:
            numero = int(input("Ingrese tu edad: "))
        except ValueError:
            print("Debes ingresar un número entero.")
            continue
        return f"Tu edad es: {numero}"

def main():
    print(pedir_entero())

main()