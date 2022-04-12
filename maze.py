import readchar
import os
import random

POS_X = 0
POS_Y = 1

NUM_OF_MAP_OBJECTS = 4
loop = True
map_objects = []
trainers = [1, 2, 3, 4]
my_position = [3, 1]

obstacle_definition = """\
###           ######
###             ####
##   #     #      ##
########        ####
##              ####
##   #####        ##
## #####       #####
#            #     #
        #       ####
#       ######    ##
###        #########
####            ####
######           ###
#           ########
####         #######\
"""

# obstacles
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

HEIGHT = len(obstacle_definition)
WIDTH = len(obstacle_definition[0])

while len(map_objects) < NUM_OF_MAP_OBJECTS:
        new_position = [random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)]

        if new_position not in map_objects and new_position != my_position and \
        obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            map_objects.append(new_position)

# Loop
while len(map_objects) > 0:

    print("+" + "-" * WIDTH * 3 + "+")

    if my_position[POS_X] < 0:
        my_position[POS_X] += WIDTH
    elif my_position[POS_X] > 20:
        my_position[POS_X] -= WIDTH
    elif my_position[POS_Y] > HEIGHT - 1:
        my_position[POS_Y] -= HEIGHT
    elif my_position[POS_Y] < 0:
        my_position[POS_Y] += HEIGHT

    if len(map_objects) > 0:
        for coordinate_y in range(HEIGHT):
            print("|", end="")

            for coordinate_x in range(WIDTH):
                charm_to_draw = "   "

                for map_object in map_objects:
                    if my_position in map_objects:
                        map_objects.remove(my_position)

                        numero = random.choice(trainers)
                        os.system("cls")

                        if numero == 1:
                                trainers.remove(1)
                                vida_inicial_pikachu = int(80)
                                vida_inicial_squirtle = int(90)
                                vida_actual_pikachu = vida_inicial_pikachu
                                vida_actual_squirtle = vida_inicial_squirtle
                                vida_faltante_pikachu = int(0)
                                vida_faltante_squirtle = int(0)

                                print("\nEmpieza el combate 1!\n"
                                      "La vida de pikachu es de [{}] ({}) y la de squirtle de [{}] ({})"
                                      .format("#" * int(vida_inicial_pikachu / 4), vida_inicial_pikachu,
                                              "#" * int(vida_inicial_squirtle / 4), vida_inicial_squirtle))
                                input("Enter para continuar...\n")

                                os.system("cls")

                                while vida_actual_squirtle >= 0 or vida_actual_pikachu >= 0:
                                    print("Turno de Pikachu")
                                    ataque_pikachu = random.randint(1, 2)
                                    if ataque_pikachu == "1":
                                        print("Pikachu ha usado Onda Voltio")
                                        vida_actual_squirtle -= 10
                                    else:
                                        print("Pikachu ha usado Bola Voltio")
                                        vida_actual_squirtle -= 11
                                    input("Enter para continuar...\n\n")
                                    os.system("cls")

                                    vida_faltante_squirtle = int(vida_inicial_squirtle / 4) - int(vida_actual_squirtle / 4)

                                    if vida_actual_squirtle < 0:
                                        vida_actual_squirtle = 0
                                        break

                                    print("La vida de squirtle es de [{}]  {}".format(
                                        "#" * int(vida_actual_squirtle / 4) + " " * vida_faltante_squirtle,
                                        vida_actual_squirtle))
                                    input("Enter para continuar...\n\n")
                                    os.system("cls")

                                    ataque_squirtle = None

                                    vida_faltante_pikachu = int(vida_inicial_pikachu / 4) - int(vida_actual_pikachu / 4)

                                    print("Turno de Squirtle\n")
                                    while ataque_squirtle != "A" and ataque_squirtle != "P" and ataque_squirtle != "B" and ataque_squirtle != "N":
                                        ataque_squirtle = input(
                                            "Elige el ataque: [P]lacaje, Pistola [A]gua, [B]urbuja, [N]ada: ")
                                    if ataque_squirtle == "P":
                                        print("Squirtle usa Placaje")
                                        vida_actual_pikachu -= 10
                                    elif ataque_squirtle == "A":
                                        print("Squirtle usa Pistola Agua")
                                        vida_actual_pikachu -= 11
                                    elif ataque_squirtle == "N":
                                        print("Squirtle no hace nada")
                                    else:
                                        print("Squirtle usa Burbuja")
                                        vida_actual_pikachu -= 9
                                    input("Enter para continuar...\n\n")
                                    os.system("cls")

                                    if vida_actual_pikachu < 0:
                                        vida_actual_pikachu = 0
                                        break

                                    print("La vida actual de pikachu es de [{}]  {}".format(
                                        "#" * int(vida_actual_pikachu / 4) + " " * vida_faltante_pikachu
                                        , vida_actual_pikachu))
                                    input("Enter para continuar...\n\n")
                                    os.system("cls")

                                if vida_actual_pikachu > vida_actual_squirtle:
                                    print("Pikachu gana!")
                                    input("Enter para continuar...\n\n")
                                    os.system("cls")
                                    print("""   _____                         ____                 
  / ____|                       / __ \                
 | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
 | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
 | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   
                                                      
                                                     """)
                                    exit()
                                else:
                                    print("Squirtle gana!")

                                input("Enter para continuar...\n\n")
                                os.system("cls")

                        elif numero == 2:
                                trainers.remove(2)
                                vida_inicial_pikachu = int(84)
                                vida_inicial_squirtle = int(93)
                                vida_actual_pikachu = vida_inicial_pikachu
                                vida_actual_squirtle = vida_inicial_squirtle
                                vida_faltante_pikachu = int(0)
                                vida_faltante_squirtle = int(0)

                                print("\nEmpieza el combate!\n\n"
                                      "Charmander vs Squirtle \n \n"
                                      "La vida de charmader es de [{}] ({}) y la de squirtle de [{}] ({})"
                                      .format("#" * int(vida_inicial_pikachu / 4), vida_inicial_pikachu,
                                              "#" * int(vida_inicial_squirtle / 4), vida_inicial_squirtle))
                                input("Enter para continuar...\n")

                                os.system("cls")

                                while vida_actual_squirtle >= 0 or vida_actual_pikachu >= 0:
                                    print("Turno de Charmander")
                                    ataque_pikachu = random.randint(1, 3)
                                    if ataque_pikachu == "1":
                                        print("Charmander ha usado Llamarada")
                                        vida_actual_squirtle -= random.randint(11, 13)
                                    elif ataque_pikachu == "2":
                                        print("Charmander ha usado garra dragon")
                                        vida_actual_squirtle -= random.randint(10, 15)
                                    else:
                                        print("Charmander ha usado arañazo")
                                        vida_actual_squirtle -= random.randint(7, 9)
                                    input("Enter para continuar...\n\n")
                                    os.system("cls")

                                    vida_faltante_squirtle = int(vida_inicial_squirtle / 4) - int(vida_actual_squirtle / 4)

                                    if vida_actual_squirtle < 0:
                                        vida_actual_squirtle = 0
                                        break

                                    print("La vida de squirtle es de [{}]  {}".format(
                                        "#" * int(vida_actual_squirtle / 4) + " " * vida_faltante_squirtle,
                                        vida_actual_squirtle))
                                    input("Enter para continuar...\n\n")
                                    os.system("cls")

                                    ataque_squirtle = None

                                    vida_faltante_pikachu = int(vida_inicial_pikachu / 4) - int(vida_actual_pikachu / 4)

                                    print("Turno de Squirtle\n")
                                    while ataque_squirtle != "A" and ataque_squirtle != "P" and ataque_squirtle != "B" \
                                            and ataque_squirtle != "N" and ataque_squirtle != "S":
                                        os.system("cls")
                                        ataque_squirtle = input(
                                            "Elige el ataque: [P]lacaje, Pistola [A]gua, [B]urbuja, [S]urf, [N]ada: ")
                                    if ataque_squirtle == "P":
                                        print("Squirtle usa Placaje")
                                        vida_actual_pikachu -= random.randint(10, 11)
                                    elif ataque_squirtle == "A":
                                        print("Squirtle usa Pistola Agua")
                                        vida_actual_pikachu -= random.randint(11, 13)
                                    elif ataque_squirtle == "N":
                                        print("Squirtle no hace nada")
                                    elif ataque_squirtle == "S":
                                        print("Squirtle usa Surf")
                                        vida_actual_pikachu -= random.randint(12, 14)
                                    else:
                                        print("Squirtle usa Burbuja")
                                        vida_actual_pikachu -= random.randint(7, 9)
                                    input("Enter para continuar...\n\n")
                                    os.system("cls")

                                    if vida_actual_pikachu < 0:
                                        vida_actual_pikachu = 0
                                        break

                                    print("La vida actual de charmander es de [{}]  {}".format(
                                        "#" * int(vida_actual_pikachu / 4) + " " * vida_faltante_pikachu
                                        , vida_actual_pikachu))
                                    input("Enter para continuar...\n\n")
                                    os.system("cls")

                                if vida_actual_pikachu > vida_actual_squirtle:
                                    print("Charmander gana!")
                                    input("Enter para continuar...\n\n")
                                    os.system("cls")
                                    print("""   _____                         ____                 
  / ____|                       / __ \                
 | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
 | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
 | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   
                                                      
                                                     """)
                                    exit()
                                else:
                                    print("Squirtle gana!")

                                input("Enter para continuar...\n\n")
                                os.system("cls")

                        elif numero == 3:
                                trainers.remove(3)
                                vida_inicial_pikachu = int(50)
                                vida_inicial_squirtle = int(100)
                                vida_actual_pikachu = vida_inicial_pikachu
                                vida_actual_squirtle = vida_inicial_squirtle
                                vida_faltante_pikachu = int(0)
                                vida_faltante_squirtle = int(0)

                                print("\nEmpieza el combate!\n"
                                      "\nDragonite vs Pikachu\n\n"
                                      "La vida de dragonite es de [{}] ({}) y la de squirtle de [{}] ({})"
                                      .format("#" * int(vida_inicial_pikachu / 4), vida_inicial_pikachu,
                                              "#" * int(vida_inicial_squirtle / 4), vida_inicial_squirtle))
                                input("Enter para continuar...\n")

                                os.system("cls")

                                while vida_actual_squirtle >= 0 or vida_actual_pikachu >= 0:
                                    print("Turno de Dragonite")
                                    ataque_pikachu = random.randint(1, 11)
                                    if ataque_pikachu == "1":
                                        print("Dragonite ha usado Garra dragon Pero falla")
                                    elif ataque_pikachu == "2":
                                        print("Dragonite ha usado Garra dragon Pero falla")
                                    elif ataque_pikachu == "3":
                                        print("Dragonite ha usado Garra dragon Pero falla")
                                    elif ataque_pikachu == "4":
                                        print("Dragonite ha usado Garra dragon Pero falla")
                                    elif ataque_pikachu == "5":
                                        print("Dragonite ha usado Garra dragon Pero falla")
                                    elif ataque_pikachu == "6":
                                        print("Dragonite ha usado Garra dragon Pero falla")
                                    elif ataque_pikachu == "7":
                                        print("Dragonite ha usado Garra dragon Pero falla")
                                    elif ataque_pikachu == "8":
                                        print("Dragonite ha usado Garra dragon Pero falla")
                                    elif ataque_pikachu == "9":
                                        print("Dragonite ha usado Garra dragon Pero falla")
                                    elif ataque_pikachu == "10":
                                        print("Dragonite ha usado Garra dragon Pero falla")
                                    else:
                                        print("Dragonite ha usado Garra dragon")
                                        vida_actual_squirtle -= 100
                                    input("Enter para continuar...\n\n")
                                    os.system("cls")

                                    vida_faltante_squirtle = int(vida_inicial_squirtle / 4) - int(vida_actual_squirtle / 4)

                                    if vida_actual_squirtle < 0:
                                        vida_actual_squirtle = 0
                                        break

                                    print("La vida de squirtle es de [{}]  {}".format(
                                        "#" * int(vida_actual_squirtle / 4) + " " * vida_faltante_squirtle,
                                        vida_actual_squirtle))
                                    input("Enter para continuar...\n\n")
                                    os.system("cls")

                                    ataque_squirtle = None

                                    vida_faltante_pikachu = int(vida_inicial_pikachu / 4) - int(vida_actual_pikachu / 4)

                                    print("Turno de Squirtle\n")
                                    while ataque_squirtle != "A" and ataque_squirtle != "P" and ataque_squirtle != "B" and ataque_squirtle != "N":
                                        ataque_squirtle = input(
                                            "Elige el ataque: [P]lacaje, Pistola [A]gua, [B]urbuja, [N]ada: ")
                                    if ataque_squirtle == "P":
                                        print("Squirtle usa Placaje")
                                        vida_actual_pikachu -= random.randint(1, 20)
                                    elif ataque_squirtle == "A":
                                        print("Squirtle usa Pistola Agua")
                                        vida_actual_pikachu -= random.randint(1, 20)
                                    elif ataque_squirtle == "N":
                                        print("Squirtle no hace nada")
                                    else:
                                        print("Squirtle usa Burbuja")
                                        vida_actual_pikachu -= random.randint(1, 20)
                                    input("Enter para continuar...\n\n")
                                    os.system("cls")

                                    if vida_actual_pikachu < 0:
                                        vida_actual_pikachu = 0
                                        break

                                    print("La vida actual de dragonite es de [{}]  {}".format(
                                        "#" * int(vida_actual_pikachu / 4) + " " * vida_faltante_pikachu
                                        , vida_actual_pikachu))
                                    input("Enter para continuar...\n\n")
                                    os.system("cls")

                                if vida_actual_pikachu > vida_actual_squirtle:
                                    print("Dragonite gana!")
                                    input("Enter para continuar...\n\n")
                                    os.system("cls")
                                    print("""   _____                         ____                 
  / ____|                       / __ \                
 | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
 | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
 | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   
                                                      
                                                     """)
                                    exit()
                                else:
                                    print("Squirtle gana!")

                                input("Enter para continuar...\n\n")
                                os.system("cls")

                        elif numero == 4:
                                trainers.remove(4)
                                vida_inicial_pikachu = int(50)
                                vida_inicial_squirtle = int(80)
                                vida_actual_pikachu = vida_inicial_pikachu
                                vida_actual_squirtle = vida_inicial_squirtle
                                vida_faltante_pikachu = int(0)
                                vida_faltante_squirtle = int(0)

                                print("\nEmpieza el combate!\n"
                                      "\nRatatta vs Squirtle\n\n"
                                      "La vida de ratatta es de [{}] ({}) y la de squirtle de [{}] ({})"
                                      .format("#" * int(vida_inicial_pikachu / 4), vida_inicial_pikachu,
                                              "#" * int(vida_inicial_squirtle / 4), vida_inicial_squirtle))
                                input("Enter para continuar...\n")

                                os.system("cls")

                                while vida_actual_squirtle >= 0 or vida_actual_pikachu >= 0:
                                    print("Turno de ratatta")
                                    ataque_pikachu = random.randint(1, 4)
                                    if ataque_pikachu == "1":
                                        print("Ratatta ha usado mordisco")
                                        vida_actual_squirtle -= random.randint(2, 4)
                                    elif ataque_pikachu == "2":
                                        print("Ratatta ha usado mordisco")
                                        vida_actual_squirtle -= random.randint(2, 4)
                                    elif ataque_pikachu == "3":
                                        print("Ratatta ha usado mordisco")
                                        vida_actual_squirtle -= random.randint(2, 4)
                                    else:
                                        print("Ratatta ha usado placaje")
                                        vida_actual_squirtle -= (random.randint(60, 70))
                                    input("Enter para continuar...\n\n")
                                    os.system("cls")

                                    vida_faltante_squirtle = int(vida_inicial_squirtle / 4) - int(vida_actual_squirtle / 4)

                                    if vida_actual_squirtle < 0:
                                        vida_actual_squirtle = 0
                                        break

                                    print("La vida de squirtle es de [{}]  {}".format(
                                        "#" * int(vida_actual_squirtle / 4) + " " * vida_faltante_squirtle,
                                        vida_actual_squirtle))
                                    input("Enter para continuar...\n\n")
                                    os.system("cls")

                                    ataque_squirtle = None

                                    vida_faltante_pikachu = int(vida_inicial_pikachu / 4) - int(vida_actual_pikachu / 4)

                                    print("Turno de Squirtle\n")
                                    while ataque_squirtle != "A" and ataque_squirtle != "P" and ataque_squirtle != "B" and ataque_squirtle != "N":
                                        ataque_squirtle = input(
                                            "Elige el ataque: [P]lacaje, Pistola [A]gua, [B]urbuja, [N]ada: ")
                                    if ataque_squirtle == "P":
                                        print("Squirtle usa Placaje")
                                        vida_actual_pikachu -= 30
                                    elif ataque_squirtle == "A":
                                        print("Squirtle usa Pistola Agua")
                                        vida_actual_pikachu -= random.randint(1, 30)
                                    elif ataque_squirtle == "N":
                                        print("Squirtle no hace nada")
                                    else:
                                        print("Squirtle usa Burbuja")
                                        vida_actual_pikachu -= 1
                                    input("Enter para continuar...\n\n")
                                    os.system("cls")

                                    if vida_actual_pikachu < 0:
                                        vida_actual_pikachu = 0
                                        break

                                    print("La vida actual de ratatta es de [{}]  {}".format(
                                        "#" * int(vida_actual_pikachu / 4) + " " * vida_faltante_pikachu
                                        , vida_actual_pikachu))
                                    input("Enter para continuar...\n\n")
                                    os.system("cls")

                                if vida_actual_pikachu > vida_actual_squirtle:
                                    print("ratatta gana!")
                                    input("Enter para continuar...\n\n")
                                    os.system("cls")
                                    print("""   _____                         ____                 
  / ____|                       / __ \                
 | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
 | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
 | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   
                                                      
                                                     """)
                                    exit()
                                else:
                                    print("Squirtle gana!")

                                input("Enter para continuar...\n\n")
                                os.system("cls")

                    if coordinate_x == map_object[POS_X] and coordinate_y == map_object[POS_Y]:
                        charm_to_draw = " * "

                if coordinate_x == my_position[POS_X] and coordinate_y == my_position[POS_Y]:
                    charm_to_draw = " @ "

                elif obstacle_definition[coordinate_y][coordinate_x] == "#":
                    charm_to_draw = "###"

                if len(map_objects) > 0:
                    print("{}".format(charm_to_draw), end="")
                else:
                    pass
            if len(map_objects) > 0:
                print("|")
            else:
                pass
        if len(map_objects) > 0:
            print("+" + "-" * WIDTH * 3 + "+")
        else:
            pass

    direction = readchar.readchar().decode()

    new_position = None

    if direction == "w":
        new_position = [my_position[POS_X], my_position[POS_Y] - 1]
    elif direction == "s":
        new_position = [my_position[POS_X], my_position[POS_Y] + 1]
    elif direction == "a":
        new_position = [my_position[POS_X] - 1, my_position[POS_Y]]
    elif direction == "d":
        new_position = [my_position[POS_X] + 1, my_position[POS_Y]]
    elif direction == "q":
         break

    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            my_position = new_position

    os.system("cls")

os.system("cls")
print("Felicidades, has vencido a todos los entrnadores pokemon!")