import csv

with open('estudiantes.csv', mode='r', encoding='utf-8') as archivo:
    archivo = csv.DictReader(archivo)
    for fila in archivo:
        print(fila['nombre'])