import re;

def main():
    correo = input("Por favor, ingresa tu correo electrónico: ")
    if re.search(r"@uai.edu.ar$", correo):
        print("Correo válido.")
    else:
        print("Correo inválido.")

main()