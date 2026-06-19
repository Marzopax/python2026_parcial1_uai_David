import sys

if len(sys.argv) != 2:
    sys.exit("Error: Se esperaba exactamente un argumento adicional.")

argumento_adicional = sys.argv[1]

print(f"¡Todo correcto! El argumento ingresado es: {argumento_adicional}")