palavras_forca = [
    "python",
    "programacao",
    "desenvolvedor",
    "computador",
    "algoritmo",
    "linguagem",
    "sintaxe",
    "compilador",
    "biblioteca",
    "framework"
]

with open("gabarito_forca.txt", "w") as file:
    for palavra in palavras_forca:
        file.write(palavra + "\n")

print("Arquivo gabarito_forca.txt criado com sucesso.")

import requests

url = "https://github.com/camilalaranjeira/python-basico-exercicios/raw/main/modulo7/gabarito_enforcado.txt"
response = requests.get(url)

with open("gabarito_enforcado.txt", "wb") as file:
    file.write(response.content)

print("Arquivo gabarito_enforcado.txt baixado com sucesso.")

import random

# Função para carregar as palavras do arquivo
def carregar_palavras(nome_arquivo):
    with open(nome_arquivo, "r") as arquivo:
        palavras = arquivo.read().splitlines()
    return palavras

# Função principal do jogo da forca
def jogar_forca():
    # Carregar palavras e selecionar uma aleatoriamente
    palavras = carregar_palavras("gabarito_forca.txt")
    palavra_secreta = random.choice(palavras).upper()
    
    # Inicializar variáveis do jogo
    letras_acertadas = ["_" for _ in palavra_secreta]
    letras_erradas = []
    tentativas = 6
    
    # Função para exibir o estado atual do jogo
    def mostrar_estado():
        print("Palavra: " + " ".join(letras_acertadas))
        print(f"Erros: {', '.join(letras_erradas)}")
        print(f"Tentativas restantes: {tentativas}")
    
    # Loop principal do jogo
    while tentativas > 0 and "_" in letras_acertadas:
        mostrar_estado()
        chute = input("Digite uma letra: ").upper()
        
        if chute in palavra_secreta:
            for idx, letra in enumerate(palavra_secreta):
                if letra == chute:
                    letras_acertadas[idx] = chute
        else:
            if chute not in letras_erradas:
                letras_erradas.append(chute)
                tentativas -= 1
            else:
                print("Você já tentou essa letra.")
    
    # Mostrar resultado final
    if "_" not in letras_acertadas:
        print(f"Parabéns! Você acertou a palavra: {palavra_secreta}")
    else:
        print(f"Você perdeu! A palavra era: {palavra_secreta}")

# Iniciar o jogo
jogar_forca()
