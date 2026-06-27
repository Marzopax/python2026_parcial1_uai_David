import re

def validar_email(email):
    if re.search(r'^\w+@uai\.edu\.ar$', email):
        print("Correo valido")
    else:
        print("Correo invalido")

def main():
    email = input("Ingrese su correo: ")
    validar_email(email)

main()    