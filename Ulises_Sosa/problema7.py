import sys
def main():
    if len(sys.argv) != 2:
        print("Error, se esperaba exactamente un argumento adicional")
        sys.exit()
    else:
        print("Exito, se recibió el argumento:", sys.argv[1])

main()

