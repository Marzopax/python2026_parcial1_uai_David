# import sys

# if (sys.argv) == 1:
#     print("argumentos suficientes")
# else:
#     print("argumentos insuficientes")
#     sys.exit()

# CORREGIDO
import sys

def val_argumentos():
    if len(sys.argv) != 2:
        sys.exit("Error: Debe agregar solo un argumento.")
    print("Argumento correcto:", sys.argv[1])

val_argumentos()