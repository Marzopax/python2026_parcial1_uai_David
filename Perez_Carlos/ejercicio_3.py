palabras = ["hola", "mundo", "python"]

for palabra in palabras:
    palabras_mayus = palabras_mayus.append(palabra.upper())

print(*palabras_mayus)