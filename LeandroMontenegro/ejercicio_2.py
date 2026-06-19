
def main():

    def pedir_entero():
        while True:
            try:
                edad = int(input("ngresa tu edad: "))
                return edad
            except ValueError:
                print("Error: ingresa un número válido.")
                break;
main()