import re

correo = input("Ingrese su correo: ")

if re.search(r"@uai\.edu\.ar$", correo):
    print("Correo válido")
else:
    print("Correo inválido")