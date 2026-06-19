import re 

correo = input("Ingrese su correo: ")

if re.search(r"@uai\.edu\.ar$",correo):
    print("Correo ingresado correctamente.")
else:
    print("Correco incorrecto.")