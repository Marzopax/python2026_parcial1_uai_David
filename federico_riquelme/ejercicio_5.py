## Problema 5: Manejo de archivos y librería CSV
##Escribí un fragmento de código que utilice el gestor de contexto `with open(...)` para abrir un archivo existente llamado `estudiantes.csv` en modo lectura.

##El programa debe:
##Importar la librería `csv`.
##Utilizar `csv.DictReader`.
##Iterar sobre las filas del archivo.
##Imprimir el valor de la columna `"nombre"` de cada registro.

### Ejemplo de archivo `estudiantes.csv`
##nombre,casa
##Ana,Gryffindor
##Zack,Slytherin

def extractor():
    import csv

    with open('estudiantes.csv', mode='r') as archivo:
        archivo_leido = csv.DictReader(archivo)
        for registro in archivo_leido:
            print(registro['nombre'])
extractor()

