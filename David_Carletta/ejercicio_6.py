# CORREGIDO
import re

def validar_correo():
    correo = input("Ingrese su correo: ")
    
    if re.search(r"@uai\.edu\.ar$", correo):
        print("Correo valido.")
    else:
        print("Correo invalido.")

validar_correo()