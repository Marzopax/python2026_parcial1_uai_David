
def main():


        while True:
            try:
                edad = int(input("ingresa tu edad: "))
                print(f"Tu edad es: {edad}")
                break;
            except ValueError:
                print("Error: ingresa un número válido.")
main()