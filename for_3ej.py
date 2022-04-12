import string

texto = input("Introduzca el texto: ")
letras_mayusculas = 0 

for letra in texto:
    if letra in string.ascii_uppercase:
        letras_mayusculas += 1
print("La mayusculas son {}".format(letras_mayusculas))