import csv

with open("estudiantes.csv", mode="r", encoding="utf-8") as archivo:
    lector_csv = csv.DictReader(archivo)
    for fila in lector_csv:
        print(fila["nombre"])