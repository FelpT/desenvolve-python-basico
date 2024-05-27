# Solicita ao usuário uma quantidade indefinida de números inteiros
numeros = []
while len(numeros) < 4:
    try:
        num = int(input("Digite um número inteiro: "))
        numeros.append(num)
    except ValueError:
        print("Por favor, digite apenas números inteiros.")

# Imprime a lista original
print("Lista original:", numeros)

# Imprime os 3 primeiros elementos
print("Os 3 primeiros elementos:", numeros[:3])

# Imprime os 2 últimos elementos
print("Os 2 últimos elementos:", numeros[-2:])

# Imprime a lista invertida
print("Lista invertida:", numeros[::-1])

# Imprime os elementos de índice par
print("Elementos de índice par:", numeros[::2])

# Imprime os elementos de índice ímpar
print("Elementos de índice ímpar:", numeros[1::2])
