texto = input("Introduce el texto: ")
espacio_numero = 0
punto_numero = 0
coma_numero = 0

for a in texto:
    if a == " ":
        espacio_numero += 1
    elif a == ".":
        punto_numero += 1
    elif a == ",":
        coma_numero += 1
print(f"Espacios: {espacio_numero}, Puntos: {punto_numero}, Comas {coma_numero}")
