import os
import re

# Define o nome dos arquivos
nome_arquivo_entrada = "frase.txt"
nome_arquivo_saida = "palavras.txt"

# Lê o conteúdo do arquivo de entrada
with open(nome_arquivo_entrada, "r") as arquivo:
    conteudo = arquivo.read()

# Remove caracteres não alfabéticos e separa as palavras
palavras = re.findall(r'\b[A-Za-zÀ-ÿ]+\b', conteudo)

# Salva as palavras no arquivo de saída, uma por linha
with open(nome_arquivo_saida, "w") as arquivo:
    for palavra in palavras:
        arquivo.write(palavra + "\n")

# Imprime o conteúdo do arquivo de saída
with open(nome_arquivo_saida, "r") as arquivo:
    conteudo_saida = arquivo.read()
    print(conteudo_saida)
