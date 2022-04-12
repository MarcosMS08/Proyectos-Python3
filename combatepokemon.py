from random import randint
import os
from traceback import print_tb



VIDA_INICIAL_PIKACHU = 80
VIDA_INICIAL_SQUIRTEL = 90

vida_pikachu = VIDA_INICIAL_PIKACHU
vida_squirtel = VIDA_INICIAL_SQUIRTEL

while vida_pikachu > 0 and vida_squirtel > 0:
    #EL COMBATE SIGUE
    print("Turno de pikachu")
    ataque_de_pikachu = randint(1, 2)
    if ataque_de_pikachu == 1:
        vida_squirtel -= 10
        print("Pikachu ataca con Bola Voltio: La vida de Squirtel baja 10")
        
    else:
        vida_squirtel -= 11
        print("Pikachu usa Onda Trueno: La vida de Squirtel baja 11")


    
    barras_de_vida_pikachu = int(vida_pikachu * 10 / VIDA_INICIAL_PIKACHU)
    print("Pikachu:   [{}{}] ({}/{})".format("#" * barras_de_vida_pikachu, " " * (10 - barras_de_vida_pikachu),
                                            vida_pikachu, VIDA_INICIAL_PIKACHU))

    barras_de_vida_squirtel = int(vida_squirtel * 10 / VIDA_INICIAL_SQUIRTEL)
    print("Squirtel   [{}{}] ({}/{})".format("#" * barras_de_vida_squirtel, " " * (10 - barras_de_vida_squirtel),
                                            vida_squirtel, VIDA_INICIAL_SQUIRTEL))

    input("Pon un Enter...\n\n")
    os.system("cls")

    #Turno de Squirtel
    print("Turno de Squirtel")
    ataque_de_squirtel = None
    while ataque_de_squirtel not in ["A", "B", "C", "D"]:
        ataque_de_squirtel = input("Pon una opcion: [A]-Placaje, [B]-Pistola Agua, [C]-Burbuja o [D]-Nada: ")
    if ataque_de_squirtel == "A":
            print("Squirtel ataca con placaje")
            vida_pikachu -= 10
            
    elif ataque_de_squirtel == "B":
            print("Squirtel ataca con Pistola Agua")
            vida_pikachu -= 12  
    elif ataque_de_squirtel == "C":
            print("Squirtel ataca con Burbuja")
            vida_pikachu -= 9
    elif ataque_de_squirtel == "D":
        print("Squirtel no ha atacado")
if vida_pikachu < 0:
    vida_pikachu = 0

if vida_squirtel < 0:
    vida_squirtel = 0

barras_de_vida_pikachu = int(vida_pikachu * 10 / VIDA_INICIAL_PIKACHU)
print("Pikachu:   [{}{}] ({}/{})".format("#" * barras_de_vida_pikachu, " " * (10 - barras_de_vida_pikachu),
                                            vida_pikachu, VIDA_INICIAL_PIKACHU))

barras_de_vida_squirtel = int(vida_squirtel * 10 / VIDA_INICIAL_SQUIRTEL)
print("Squirtel   [{}{}] ({}/{})".format("#" * barras_de_vida_squirtel, " " * (10 - barras_de_vida_squirtel),
                                            vida_squirtel, VIDA_INICIAL_SQUIRTEL))

input("Pon un Enter...\n\n")

os.system("cls")

if vida_squirtel > vida_pikachu:
    print("Squirtel gana!!!")
else:
    print("Pikachu gana!!!")
