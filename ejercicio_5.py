import csv
with open("estudiantes.csv") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        print(fila["nombre"])