## Problema 6: Expresiones regulares
##Asumiendo que importaste la biblioteca `re`, escribí una instrucción condicional `if` que utilice la función `re.search()` para validar si una variable `correo`, ingresada por el usuario, termina estrictamente en:
##@uai.edu.ar

##El programa debe:

##Usar el anclaje de fin de línea `$`.
##Escapar correctamente los puntos con `\.` para que sean interpretados como caracteres literales.
##Mostrar un mensaje indicando si el correo es válido o inválido.

def validador():
    import re
    correo = input("Ingresa tu correo: ")
    if re.search(r"@uai\.edu\.ar$", correo):
        print("Correo válido.")
    else:
        print("Correo inválido.")
validador()