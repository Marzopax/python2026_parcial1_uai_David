def convertirMayusculas(lista):
    nueva_lista = []
    for i in lista:
        nueva_lista.append(str(i).upper())
    return nueva_lista

def main():
    palabras = ["hola", "mundo", "python"]
    mayusculas= convertirMayusculas(palabras)
    for m in mayusculas:
        print(m)

if __name__ == "__main__":
    main()