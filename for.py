lista_compra = ["leche", "arroz", "jamon"]
frase = "hola, hoy estoy aprendiendo pythohn"
vocales = ["a", "e", "i", "o", "u"]
vocales_numero = 0
for item in lista_compra:
    print("Hoy voy a comprar {}".format(item))
for letra in frase:
    print(letra)
for letra in frase:
    if letra in vocales:
        print("He encontrado una '{}'".format(letra))
        vocales_numero += 1
print("Vocales encontradas: {}".format(vocales_numero))