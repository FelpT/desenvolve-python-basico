import random

# Função para preencher uma lista com valores inteiros aleatórios entre 0 e 50
def preencher_lista():
    return [random.randint(0, 50) for _ in range(20)]

# Função para encontrar a interseção entre duas listas
def encontrar_interseccao(lista1, lista2):
    return list(set(lista1) & set(lista2))

# Função para contar a ocorrência de cada elemento em uma lista
def contar_ocorrencias(lista):
    contador = {}
    for elemento in lista:
        if elemento in contador:
            contador[elemento] += 1
        else:
            contador[elemento] = 1
    return contador

# Preencher as listas
lista1 = preencher_lista()
lista2 = preencher_lista()

# Encontrar a interseção entre as listas
interseccao = encontrar_interseccao(lista1, lista2)

# Ordenar a lista de interseção
interseccao.sort()

# Contar as ocorrências de cada elemento nas duas listas
contagem_lista1 = contar_ocorrencias(lista1)
contagem_lista2 = contar_ocorrencias(lista2)

# Imprimir resultados
print("lista1 -", lista1)
print("lista2 -", lista2)
print("Interseccao -", interseccao)
print("Contagem")
for elemento in interseccao:
    print(f"{elemento}: (lista1={contagem_lista1.get(elemento, 0)}, lista2={contagem_lista2.get(elemento, 0)})")
