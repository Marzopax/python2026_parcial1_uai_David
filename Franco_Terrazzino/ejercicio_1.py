def IngresarNombre():
    nombre = input("Ingrese su nombre: ").strip().title()
    print(f"Hola, {nombre}")
    
def main():
    IngresarNombre()

if __name__=="__main__":
    main()