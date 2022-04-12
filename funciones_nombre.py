pon_nombre = str(input("Cual es tu nombre: "))

def saludo_sectario(nombre):
    print(f"Hola {nombre[::-1]}")

saludo_sectario(pon_nombre)