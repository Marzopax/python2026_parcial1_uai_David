import csv

with open(r"C:\Users\Navegador\Downloads\estudiantes.csv", mode="r", encoding="utf-8") as archivo:
    
    lector_dict = csv.DictReader(archivo)
    
    for fila in lector_dict:
        print(fila["nombre"])
        
        