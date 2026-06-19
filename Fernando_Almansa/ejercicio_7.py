import sys

if len(sys.argv) != 2:
    sys.exit("Error: debe ingresar exactamente un argumento.")

print(f"Argumento recibido: {sys.argv[1]}")