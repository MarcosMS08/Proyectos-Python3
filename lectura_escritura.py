from ssl import DER_cert_to_PEM_cert


SALIDA = "SALIR"
items_del_supermercado = []
ARBHIVO_LISTA = "lista_compra.txt"



def pregunta_user():
    return input(f"Introduce un producto [{SALIDA} para salir]: ")


def guardar_item_en_lista(lista_compra, item_a_guardar):
    if item_a_guardar.lower() in [a.lower() for a in lista_compra]:
            print("El producto ya existe!!")
    else:
        lista_compra.append(item_a_guardar)

    
def crear_archivo(lista_compra):
    
    with open(ARBHIVO_LISTA, "w") as mi_archivo:
        mi_archivo.write("\n".join(lista_compra))


def cargar_archivo():
    lista_compra = []
    if input("Te interesa cargar la ultima lista de la compra [S/N]: ") == "S":            
        try:
            with open(ARBHIVO_LISTA, "r") as a:
                lista_compra = a.read().split("\n")
        except FileNotFoundError:
            print("Archivo no encontrado!!!")
    return lista_compra
def main():       
    lista_compra = cargar_archivo()
    input_usuario = pregunta_user()
    while input_usuario != SALIDA:
        guardar_item_en_lista(lista_compra, input_usuario)
        print("\n".join(lista_compra))
        input_usuario = pregunta_user()
    crear_archivo(lista_compra)
    print(lista_compra) 
    
if __name__ == "__main__":
    main()

