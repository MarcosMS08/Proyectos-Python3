print("Elige tu movil\n"
       "1.Android\n"
       "2.iOS\n")

opcion = int(input("Elige una opcion:"))

if opcion == 1:
    print("Has elegido un Android\n")
    tienes_dinero = str(input("Tienes dinero Pon Si o No:"))
    if tienes_dinero == "Si":
        print("Te importa la camara")
        camara = str(input("Pon Si o No: "))
        if camara == "Si":
            print("El movil recomendado es Google Picel Supercamar")
        else:
            print("La opcion recomendada es Android calidad-precio")
    else:
        print("Android Chino 100 euros")
elif opcion == 2:
    print("Has elegido un iOS\n")
    tienes_dinero = str(input("Tienes dinero: Pon Si o No: "))
    if tienes_dinero == "Si":
        print("iPhone Ultra Pro Max")
    else:
        print("iPhone segunda mano")
else:
    print("Pon una opcion valida")