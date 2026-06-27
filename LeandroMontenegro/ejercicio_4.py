alumnos = [
    {"nombre": "Zack", "casa": "Slytherin"},
    {"nombre": "Ana", "casa": "Gryffindor"}
]

def main():
    for alumno in sorted(alumnos, key=lambda x: x["nombre"]):
        print(f"{alumno['nombre']}")

main()