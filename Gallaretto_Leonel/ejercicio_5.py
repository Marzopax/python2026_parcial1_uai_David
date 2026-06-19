def main():
    import csv
    with open('estudiantes.csv', mode='r') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            print(fila['nombre'])
        
main()