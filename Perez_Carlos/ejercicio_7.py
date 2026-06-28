import sys

if len(sys.argv) != 2:
    sys.exit("Error: debe ingresar un solo argumento")

archivo = sys.argv[1]
print(f"Archivo recibido: {archivo}")