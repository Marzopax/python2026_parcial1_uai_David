import sys
if len(sys.argv) != 2:
    sys.exit("Error: Debe ingresar exactamente un argumento adicional.")
argumento = sys.argv[1]
print(f"Argumento recibido ok: {argumento}")

##Ahora pongo como lo ejecute local
##PS C:\Users\Navegador\Downloads\Parcial 1 - Python - Lucas Calvo Coltro> python ejercicio_7.py archivo.txt
##Argumento recibido ok: archivo.txt