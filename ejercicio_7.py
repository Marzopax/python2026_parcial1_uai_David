## Problema 7: Argumentos de línea de comandos con `sys`
##Escribí un script que verifique si el usuario introdujo exactamente un argumento adicional al ejecutar el programa desde la terminal.
##El programa debe asumir que se importó la librería `sys`.

##Si el usuario ingresa menos argumentos o más argumentos de los esperados, el programa debe salir de inmediato imprimiendo un mensaje de error utilizando `sys.exit()`.

def verificador():
    import sys
    
    if len(sys.argv) < 3:
        print(f"Uso menos argumentos de los esperados")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print(f"Uso más argumentos de los esperados")
        sys.exit(1)
        
    argumento = sys.argv[1]
    argumento2 = sys.argv[2]
    print(f"Has ingresado correctamente los argumentos: {argumento} {argumento2}")
verificador()