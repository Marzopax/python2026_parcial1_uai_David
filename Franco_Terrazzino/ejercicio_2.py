def IngresarEdad():
    condicion = True
    while condicion:
        try:
            edad = int(input("Ingrese su edad: "))
        except ValueError:
            print("El valor ingresado debe ser numerico")
        else:
            print(f"Su edad es {edad} años")
            break

def main():
    IngresarEdad()

if __name__=="__main__":
    main()