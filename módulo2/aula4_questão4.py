#Leitura de dados(entrada)
Valor= int(input("digite o valor:"))

#processamento
notas_100= Valor//100

Valor= Valor%100

notas_50= Valor//50

Valor= Valor%50

notas_20= Valor//20

Valor= Valor%20

notas_10= Valor//10

Valor= Valor%10

notas_5= Valor//5

Valor= Valor%5

moedas_1= Valor//1

Valor= Valor%1


#impressão dos dados(saída)
print(f"{notas_100} Notas de 100")
print(f"{notas_50} Notas de 50")
print(f"{notas_20} Notas de 20")
print(f"{notas_10} Notas de 10")
print(f"{notas_5} Notas de 5")
print(f"{moedas_1} moedas de 1")
