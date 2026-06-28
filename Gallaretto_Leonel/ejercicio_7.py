
def main():
    import sys
    if len(sys.argv) != 2:
        print("Error: Se esperaba exactamente un argumento adicional.")
        sys.exit(1)
    else:
        print("Argumento válido:", sys.argv[1])
main()