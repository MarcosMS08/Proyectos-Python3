import random
numero_de_rata = random.randint(1, 100)

print("Bienvenido a La Mazmorra\n"
    "El juego consiste en rescatar a tu amigo e huir\n")

print("Hay una puerta y una trampilla por donde sales: [A]-Puerta o [B]-Trampilla\n")

barra_de_hierro = False
opc = input("Elige una opcion: [A] o [B]: ")


if opc == "A":
    print("Hay un guardia de seguridad: [A]-Te duermes o [B]-Huyes\n")
    opc2 = input("Elige una opcion: [A] o [B]: ")
    if opc2 == "A":
        print("Has perdido el guardia te ha matado\n")
        exit()
    elif opc2 == "B":
        print("Has conseguido escapar pero no has encontrado a tu amigo has perdido\n")
        exit()
elif opc == "B":
    print("Has entrado al sotano hay dos pasillos que no se ve el final en cual entras: [A]-Izquierda o [B]-Derecha\n")
    opc3 = input("Elige una opcion: [A] o [B]: ")
    if opc3 == "A":
        print("Te pierdes y mueres porque no tienes ni agua ni comida\n")
        exit()
    elif opc3 == "B":
        print("Hay una barra de hierro: [A]-La coges [B]-La dejas\n")
        opc4 = input("Elige una opcion: [A] o [B]: ") 
        if opc4 == "A":
            print("Hay una puerta pero detras hay una rata gigante: [A]-Te quedas o [B]-Luchas contra ella\n")
            barra_de_hierro = True
            opc5 = input("Elige una opcion: [A] o [B]: ")
            if opc5 == "A" :
                print("Eres deborado por las ratas mientras duermes has perdido\n")
                exit()
            elif opc5 == "B":
                print("La rata te pregunta cuanto es 12 * {}".format(numero_de_rata))
                operacion = int(input("Pon el resultado: "))
                
                if operacion == 12 * numero_de_rata and barra_de_hierro == True:
                    print("La rata te intenta atacar por acertar pero como no le gustan los listillos pero le pegas un palazo con el hierro\n"
                            "Felicidades has ganado y has rescatado a tu amigo")
                    exit()
                elif operacion != 12 * numero_de_rata:
                    print("La rata te da a tu amigo y huis\n"
                        "Felicidades has ganado!!!\n")
                    exit()
else:
    print("Elige una opcion correta [A] o [B]\n")
    exit()
