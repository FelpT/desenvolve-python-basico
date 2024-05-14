n1= int(input("Digite um número:"))
n2= int(input("Digite um número:"))
n3= int(input("Digite um número:"))

m= (n1+n2+n3)/3

if m>=60:
    print("Aprovado")
elif m>=40:
    print("Recuperação")
else:
    print("Reprovado")

print("Fim")