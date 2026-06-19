import sys

# sys.argv[0] es el nombre del script (ejercicio_07.py)
# sys.argv[1] debería ser un argumento adicional (archivo.txt) y no se permiten mas argumentos

if len(sys.argv) != 2:
    sys.exit("Error: Debes introducir exactamente un argumento adicional.")

argumento = sys.argv[1]
print("¡Éxito! Argumento recibido correctamente: ", argumento)