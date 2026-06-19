## Problema 2: Excepciones y bucles

## Implementá una función llamada `pedir_entero()` que utilice un bucle `while True` para pedirle al usuario su edad.

## El programa debe:

## - Solicitar una edad por teclado.
## - Utilizar un bloque `try...except ValueError`.
## - Detectar si el usuario ingresa texto en lugar de un número.
## - Evitar que el programa finalice con error.
## - Volver a pedir el dato hasta que sea válido.
## - Finalizar el bucle utilizando `break` o `return`.


def pedir_entero():
    edad = None
    
    while True:
        edad = input("Ingrese su edad: ")
        
        try:
            edad = int(edad)
        except ValueError:
            print("La edad ingresada no es correcta")
        else:
            break            
        
    