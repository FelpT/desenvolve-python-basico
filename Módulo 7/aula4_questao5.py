# Lista de livros com suas informações
livros = [
    ["O Alquimista", "Paulo Coelho", 1988, 208],
    ["1984", "George Orwell", 1949, 328],
    ["Dom Casmurro", "Machado de Assis", 1899, 256],
    ["A Culpa é das Estrelas", "John Green", 2012, 313],
    ["A Revolução dos Bichos", "George Orwell", 1945, 112],
    ["O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 96],
    ["Cem Anos de Solidão", "Gabriel García Márquez", 1967, 417],
    ["Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, 223],
    ["Senhora", "José de Alencar", 1875, 208],
    ["O Senhor dos Anéis: A Sociedade do Anel", "J.R.R. Tolkien", 1954, 423]
]

# Nome do arquivo CSV
nome_arquivo = "meus_livros.csv"

# Escrever os dados no arquivo CSV
with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    # Escrever os títulos das colunas
    arquivo.write("Título,Autor,Ano de publicação,Número de páginas\n")
    
    # Escrever as informações dos livros
    for livro in livros:
        linha = f"{livro[0]},{livro[1]},{livro[2]},{livro[3]}\n"
        arquivo.write(linha)

print(f"Arquivo {nome_arquivo} criado com sucesso.")
