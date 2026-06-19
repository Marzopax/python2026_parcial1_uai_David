## Problema 5: Manejo de archivos y librería CSV

## Escribí un fragmento de código que utilice el gestor de contexto `with open(...)` para abrir un archivo existente llamado `estudiantes.csv` en modo lectura.

## El programa debe:

## - Importar la librería `csv`.
## - Utilizar `csv.DictReader`.
## - Iterar sobre las filas del archivo.
## - Imprimir el valor de la columna `"nombre"` de cada registro.

### Ejemplo de archivo `estudiantes.csv`

## ```csv
## nombre,casa
## Ana,Gryffindor
## Zack,Slytherin
## ```

import csv

with open("estudiantes.csv", newline="") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print((row.split())[0] )
    
    