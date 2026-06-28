import sys

if len(sys.argv) != 2:
    print(f"Uso incorrecto. Falta un argumento adicional.")
    print(f"Ejemplo: python {sys.argv[0]} archivo.txt")
    sys.exit(1)

archivo = sys.argv[1]
print(f"Ejecucion valida con el archivo: {archivo}")
