## Problema 1: Variables y cadenas de texto

## Escribí un programa que solicite al usuario su nombre.

## El programa debe:

## - Eliminar los espacios en blanco al principio y al final del texto ingresado.
## - Convertir la primera letra de cada palabra a mayúscula.
## - Imprimir un saludo en consola utilizando cadenas formateadas `f-strings`.


name = input("Ingrese su nombre:")

name = name.strip()
name = name.capitalize()
f"Hola {name}"

