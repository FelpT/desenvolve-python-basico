import random
from collections import Counter

# Gerar duas listas com 20 valores inteiros aleatórios entre 0 e 50
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

# Encontrar a intersecção das duas listas
# Converte as listas em conjuntos para encontrar os elementos comuns
interseccao = list(set(lista1) & set(lista2))
# Ordena a lista de intersecção
interseccao.sort()

# Contar a quantidade de vezes que cada elemento aparece em cada lista
contador_lista1 = Counter(lista1)
contador_lista2 = Counter(lista2)

# Imprimir as listas e a interseção
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Interseção ordenada:", interseccao)

# Imprimir a quantidade de vezes que cada elemento aparece em cada lista
print("\nQuantidade de vezes que cada elemento aparece em Lista 1:")
for elemento, contagem in contador_lista1.items():
    print(f"Elemento {elemento}: {contagem} vez(es)")

print("\nQuantidade de vezes que cada elemento aparece em Lista 2:")
for elemento, contagem in contador_lista2.items():
    print(f"Elemento {elemento}: {contagem} vez(es)")
