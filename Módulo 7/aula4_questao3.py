import requests

url = "https://aplauso.imprensaoficial.com.br/edicoes/12.0.813.502/12.0.813.502.txt"
response = requests.get(url)

with open("estomago.txt", "wb") as file:
    file.write(response.content)

print("Arquivo baixado e salvo como estomago.txt")

# Função para ler e analisar o arquivo
def analisar_arquivo(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    # Imprimir as primeiras 25 linhas
    print("Primeiras 25 linhas do arquivo:")
    for linha in linhas[:25]:
        print(linha, end='')

    # Número de linhas do arquivo
    num_linhas = len(linhas)
    print(f"\n\nNúmero total de linhas: {num_linhas}")

    # Linha com maior número de caracteres
    linha_maior = max(linhas, key=len)
    print(f"Linha com maior número de caracteres ({len(linha_maior)} caracteres):\n{linha_maior}")

    # Contar menções aos personagens "Nonato" e "Íria"
    num_mencoes_nonato = sum(linha.lower().count("nonato") for linha in linhas)
    num_mencoes_iria = sum(linha.lower().count("íria") for linha in linhas)

    print(f"Número de menções a 'Nonato': {num_mencoes_nonato}")
    print(f"Número de menções a 'Íria': {num_mencoes_iria}")

# Nome do arquivo
nome_arquivo = "estomago.txt"

# Analisar o arquivo
analisar_arquivo(nome_arquivo)

