user_text = int(input("Pon el numero: "))
multiplo = int(input("De que quieres sacar el multiplo: "))

for numero in range(1, 11):
    if numero % multiplo == 0:
        print(f"{user_text} X {numero} = {numero * user_text}")
    
