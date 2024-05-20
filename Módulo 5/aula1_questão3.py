import random
numero_certo= random.randint(1,10)
while True:
    palpite=int(input("Adivinhe o número de 1 a 10:"))
    
    if palpite>numero_certo:
        print(f"Valor maior que o número desejado, tente novamente")
    elif palpite< numero_certo:
        print(f"Valor menor que o número desejado, tente novamente")
    else:
        print(f"Parabéns,Você acertou!")
        break    