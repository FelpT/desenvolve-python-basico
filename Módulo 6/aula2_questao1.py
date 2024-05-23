import random

# Gerar uma lista com 20 valores inteiros aleatórios entre -100 e 100
lista = [random.randint(-100, 100) for _ in range(20)]

# Ordenar a lista sem modificar a lista original
lista_ordenada = sorted(lista)

# Encontrar os índices do maior e do menor valor na lista original
indice_maior_valor = lista.index(max(lista))
indice_menor_valor = lista.index(min(lista))

# Imprimir os resultados
print("Lista original:", lista)
print("Lista ordenada:", lista_ordenada)
print("Índice do maior valor:", indice_maior_valor)
print("Índice do menor valor:", indice_menor_valor)
