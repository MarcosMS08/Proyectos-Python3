import random

numero = random.randint(1, 10)
elige_numero = int(input("Pon un número del 1 al 10: "))

if elige_numero == numero:
    print("Enhorabuena has adivinado el número ")
if elige_numero != numero:
    print("Ese no era el número el número era {}".format(numero))
if elige_numero < 1:
    print("Es de masiado pequeño prueba a poner un numero entre 1 y 10")
if elige_numero > 10:
    print("Te has pasado es entre 1 y 10")