import re
correo = input("Ingrese correo electrónico :")
if re.search(r"@uai\.edu\.ar$", correo):
    print("Correo válido")
else:
    print("Correo inválido")