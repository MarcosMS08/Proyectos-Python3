from traceback import print_tb


print("Lista de la compra")
compra = []
producto = None

while producto != "Q":
    producto = input("¿Qué desea comprar? [Q para Salir]: ")

    if producto in compra:
        print(" {} ya  esta!!!".format(producto))
    
    elif producto != "Q" and producto not in compra:
        agregar = input(f"Seguro que quieres añadir {producto} a tu lista [S/N]: ")
        print(agregar)
        if agregar == "S":
            compra.append("{}".format(producto))
        elif agregar == "N":
            print("No se ha añadido {}".format(producto))
print("La lista es: {}".format(compra))