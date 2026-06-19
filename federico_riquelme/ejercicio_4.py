## Problema 4: Funciones anónimas y ordenación con `lambda`
##Dada la siguiente lista de diccionarios:

##alumnos = [
  ##  {"nombre": "Zack", "casa": "Slytherin"},
  ##  {"nombre": "Ana", "casa": "Gryffindor"}
##]

##Escribí una única línea de código que utilice:

##Un bucle `for`.
##La función `sorted()`.
##Una función `lambda` en el parámetro `key`.
##El objetivo es recorrer la lista ordenada alfabéticamente tomando como referencia la clave `"nombre"` de cada diccionario.

def formateador():
    alumnos = [
        {"nombre": "Zack", "casa": "Slytherin"},
        {"nombre": "Ana", "casa": "Gryffindor"}
    ]
    for alumno in sorted(alumnos, key=lambda x: x["nombre"]): print(alumno["nombre"])
formateador()
