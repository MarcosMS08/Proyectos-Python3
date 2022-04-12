respuesta = None

while respuesta != "A" and respuesta != "B" and respuesta != "C": 
    respuesta = input("¿Que opcion prefieres? [A, B, C]")
    print("Esto es una prueba")

if respuesta == "A":
    print("Has elegido bien")
elif respuesta == "B":
    print("Podrias haber elgido mejor")
elif respuesta == "C":
    print("Has elegido mal")
else:
    print("No me has dado una respuesta con sentido")
