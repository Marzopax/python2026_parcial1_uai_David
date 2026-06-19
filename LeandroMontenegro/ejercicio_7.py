import sys;
def main():
    if len(sys.argv) != 2:
        print("Error: Debes ingresar exactamente un argumento adicional.")
        sys.exit(1)
    else:
        print(f"Argumento ingresado: {sys.argv[1]}")