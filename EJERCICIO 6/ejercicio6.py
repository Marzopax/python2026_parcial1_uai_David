import re
correo = input("Ingresá tu correo electrónico: ")
patron = r"@uai\.edu\.ar$"
if re.search(patron, correo):
    print("Válido: El correo pertenece al dominio @uai.edu.ar")
else:
    print("Inválido: El correo no cumple con el dominio requerido")
