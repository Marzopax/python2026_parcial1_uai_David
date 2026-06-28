## Problema 6: Expresiones regulares

## Asumiendo que importaste la biblioteca `re`, escribí una instrucción condicional `if` que utilice la función `re.search()` 
# para validar si una variable `correo`, ingresada por el usuario, termina estrictamente en:

## ```text
## @uai.edu.ar
## ```

## El programa debe:

## - Usar el anclaje de fin de línea `$`.
## - Escapar correctamente los puntos con `\.` para que sean interpretados como caracteres literales.
## - Mostrar un mensaje indicando si el correo es válido o inválido.

### Ejemplo válido

## ```text
## alumno@uai.edu.ar
## ```

### Ejemplo inválido

## ```text
## alumno@uai.com
## ```

import re

correo = input("Ingrese su correo UAI:")

correo = correo.replace(".", "\.")
if re.search("@uai.edu.ar", correo) == None:
    print("El correo no es válido")
else:
    print("El correo es válido")    
    