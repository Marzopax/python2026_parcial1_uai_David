alumnos = [
    {"nombre": "Zack", "casa": "Slytherin"},
    {"nombre": "Ana", "casa": "Gryffindor"}
]

for alumno in sorted(alumnos, key=lambda x: x["nombre"]):
    print(alumno["nombre"])