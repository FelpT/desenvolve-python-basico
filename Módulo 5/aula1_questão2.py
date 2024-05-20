import random
import math

n= int(input())
soma=0

for i in range(n):
    soma= soma+random.randint(0,100)
    print(soma)
print(f"A raiz quadrada da soma é {math.sqrt(soma):.2f}")