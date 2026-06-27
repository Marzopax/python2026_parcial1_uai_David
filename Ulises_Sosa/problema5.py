import csv

def leer_csv(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            print(fila['nombre'])

def main():
    nombre_archivo = 'estudiantes.csv'
    leer_csv(nombre_archivo)

main()