#entrada de dados
gênero= (input("M or F"))
idade= int(input("idade:"))
tempo_de_serviço= int(input("Tempo de serviço(em anos)"))
#processamento
A=(gênero=='F' and idade>=60) or (gênero=='M' and idade>=65)
B=tempo_de_serviço>=30
C= idade>=60 and tempo_de_serviço>=25
Aposentar_se= A or B or C
#saida
print(Aposentar_se)
