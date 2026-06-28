import csv
with open('estudiantes.csv', mode='r', encoding='utf-8') as file:
    lector = csv.DictReader(file)
    for line in lector:
        print(line['nombre'])