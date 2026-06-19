def pedir_entero():
    while True:
        try: 
            edad = int(input("Ingrese su edad: "))
            return edad
        except ValueError:
            print("Debe ingresar un numero valido. ")
            
edad=pedir_entero()
print(f"Edad registrada: {edad}")