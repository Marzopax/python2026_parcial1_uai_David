#Validar que sea @uai.edu.ar
import re
    
correo = input("Ingrese su correo electrónico: ")

    # Validamos el dominio @uai.edu.ar
if re.search(r"@uai\.edu\.ar$", correo):
    print("El correo es válido.")
else:
    print("El correo debe ser de domino @uai.edu.ar")