def main():
    import re
    correo = input("Ingrese su correo electrónico: ")
    if re.search(r'@uai\.edu\.ar$', correo):
        print("Correo válido.")
    else:
        print("Correo inválido.")
main()