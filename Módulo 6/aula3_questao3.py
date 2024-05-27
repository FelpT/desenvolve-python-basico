import random

# Cria uma lista com 20 elementos aleatórios entre -10 e 10
lista = [random.randint(-10, 10) for _ in range(20)]

# Imprime a lista original
print("Original:", lista)

# Encontra o intervalo com a maior quantidade de números negativos
maior_intervalo_negativo = []
inicio_intervalo = 0
for i in range(len(lista)):
    if lista[i] < 0:
        contador_negativos = 1
        for j in range(i + 1, len(lista)):
            if lista[j] < 0:
                contador_negativos += 1
            else:
                break
        if contador_negativos > len(maior_intervalo_negativo):
            maior_intervalo_negativo = lista[i:i + contador_negativos]
            inicio_intervalo = i

# Deleta o intervalo com a maior quantidade de números negativos
del lista[inicio_intervalo:inicio_intervalo + len(maior_intervalo_negativo)]

# Imprime a lista editada
print("Editada:", lista)
