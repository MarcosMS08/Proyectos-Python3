lista = []
numeros = int(input("Pon el numero: "))
lista.append(numeros)

while input("Desea introducir mas numeros [S/N]: ") == "S":
    numeros = int(input("Pon el numero: "))
    lista.append(numeros)
pequeño = lista[0]
grande = lista[0]
for numero in lista[1:]:
    if pequeño > numero:
        pequeño = numero
    if grande < numero: 
        grande = numero
print(f"Numero grande {grande}, Numero pequeño {pequeño} de {lista}")