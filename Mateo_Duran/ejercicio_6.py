import re

correo = input("Ingrese su correo: ")

if re.search(r"@uai\.edu\.ar$", correo):
    print("El correo es válido")
else:
    print("El correo es inválido")