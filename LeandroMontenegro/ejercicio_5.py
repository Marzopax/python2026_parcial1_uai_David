import csv 
def main():
    with open("estudiantes.csv", mode="r") as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            print(fila["nombre"])

main()