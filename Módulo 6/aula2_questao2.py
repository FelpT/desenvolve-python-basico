import random

# Gerar aleatoriamente um valor entre 5 e 20 e armazenar em num_elementos
num_elementos = random.randint(5, 20)

# Gerar aleatoriamente valores entre 1 e 10, na quantidade de num_elementos, e armazenar em elementos
elementos = [random.randint(1, 10) for _ in range(num_elementos)]

# Calcular a soma dos valores da lista
soma_elementos = sum(elementos)

# Calcular a média dos valores da lista
media_elementos = soma_elementos / num_elementos

# Imprimir os resultados
print("Lista elementos:", elementos)
print("Soma dos valores da lista:", soma_elementos)
print("Média dos valores da lista:", media_elementos)
