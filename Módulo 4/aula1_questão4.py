n= int(input("Digite algum valor:"))
maior= 0

while n>0:
    x=int(input("digite algum valor:"))
    if x>maior:
        maior=x
        n-=1

print("O valor de maior é",{maior})            