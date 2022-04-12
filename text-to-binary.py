separador = " " 
def Manchester_Code():
    def ascii_a_binario(letra):
        # Extraer su valor entero
        valor = ord(letra)
        # Convertirlo a binario
        return "{0:08b}".format(valor)

    def texto_a_binario(texto):
        texto_binario = ""  # El resultado
        contador = 0
        for letra in texto:
            texto_binario += ascii_a_binario(letra)
            # Agregar un espacio entre binarios, excepto si es el último carácter
            if contador + 1 < len(texto):
                texto_binario += separador
            contador += 1
        return texto_binario
    texto_original = input("")
    texto_codificado = texto_a_binario(texto_original)
    print(texto_codificado)
    