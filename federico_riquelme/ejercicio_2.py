## Problema 2: Excepciones y bucle
## Implementá una función llamada `pedir_entero()` que utilice un bucle `while True` para pedirle al usuario su edad.

##El programa debe:

##Solicitar una edad por teclado.
##Utilizar un bloque `try...except ValueError`.
##Detectar si el usuario ingresa texto en lugar de un número.
##Evitar que el programa finalice con error.
##Volver a pedir el dato hasta que sea válido.
##Finalizar el bucle utilizando `break` o `return`.
### Ejemplo esperado

##Ingrese su edad: veinte
##Debe ingresar un número válido.
##Ingrese su edad: 20
##Edad registrada: 20

def pedir_entero():   
    edad = input("Ingrese su edad:")
    while True:
        try:
            edad_formateada = int(edad)
            print(f"Edad registrada: {edad_formateada}")
            break
        except ValueError:
            print("Debe ingresar un número válido.")
            break
pedir_entero()