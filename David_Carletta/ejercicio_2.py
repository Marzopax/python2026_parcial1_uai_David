while True:
    edad = int(input("ingrese edad: "))
    try:
        edad == int()
        print("edad valida")
        break
    except ValueError:
        print("edad no valida, intente nuevamente")