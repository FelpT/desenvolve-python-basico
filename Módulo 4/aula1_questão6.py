#entrada
n= int(input())

#inicialização das variavéis e controles
cont=0
soma_sapo= sp= 0
soma_ratos=sr=0
somas_coelhos=sc=0

#interação
while cont <n:
    quantia= int(input())
    tipo= input()
    if tipo =='S':sp+=quantia
    elif tipo =='R': sr+=quantia
    elif tipo =='C': sc+= quantia

    cont+= 1

#Saídas    
print("total de cobaias", sp+sr+sc)
print("total de sapos", sp)    
print("total de ratos", sr)    
print("total de coelhos", sc)    
