# import csv

# with open(estudiantes.csv, "r") as archivo:
#     for linea in archivo:
#         csv.DictReader("nombre")
#         print(linea)

# CORREGIDO
import csv

def leer_estudiantes():
    with open("estudiantes.csv", mode="r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            print(fila["nombre"])

leer_estudiantes()