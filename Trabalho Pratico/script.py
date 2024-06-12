import csv

# Estrutura de dados para usuários e produtos
usuarios = []
produtos = []

# Funções para carregar e salvar dados em arquivos CSV

def carregar_usuarios():
    with open('usuarios.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            usuarios.append(row)

def salvar_usuarios():
    with open('usuarios.csv', 'w', newline='') as file:
        fieldnames = ['nome', 'senha', 'tipo']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(usuarios)

def carregar_produtos():
    with open('produtos.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            produtos.append(row)

def salvar_produtos():
    with open('produtos.csv', 'w', newline='') as file:
        fieldnames = ['nome', 'codigo', 'preco', 'quantidade']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(produtos)

# Funções CRUD de usuários

def criar_usuario(nome, senha, tipo):
    usuarios.append({'nome': nome, 'senha': senha, 'tipo': tipo})
    salvar_usuarios()

def listar_usuarios():
    for usuario in usuarios:
        print(usuario)

def atualizar_usuario(nome, senha, tipo):
    for usuario in usuarios:
        if usuario['nome'] == nome:
            usuario['senha'] = senha
            usuario['tipo'] = tipo
            salvar_usuarios()
            break

def deletar_usuario(nome):
    for usuario in usuarios:
        if usuario['nome'] == nome:
            usuarios.remove(usuario)
            salvar_usuarios()
            break

# Funções CRUD de produtos

def criar_produto(nome, codigo, preco, quantidade):
    produtos.append({'nome': nome, 'codigo': codigo, 'preco': preco, 'quantidade': quantidade})
    salvar_produtos()

def listar_produtos():
    for produto in produtos:
        print(produto)

def atualizar_produto(codigo, novo_nome, novo_preco, nova_quantidade):
    for produto in produtos:
        if produto['codigo'] == codigo:
            produto['nome'] = novo_nome
            produto['preco'] = novo_preco
            produto['quantidade'] = nova_quantidade
            salvar_produtos()
            break

def deletar_produto(codigo):
    for produto in produtos:
        if produto['codigo'] == codigo:
            produtos.remove(produto)
            salvar_produtos()
            break

def buscar_produto_por_nome(nome):
    for produto in produtos:
        if produto['nome'].lower() == nome.lower():
            print(produto)

def ordenar_produtos_por_nome():
    produtos_ordenados = sorted(produtos, key=lambda x: x['nome'])
    for produto in produtos_ordenados:
        print(produto)

def ordenar_produtos_por_preco():
    produtos_ordenados = sorted(produtos, key=lambda x: float(x['preco']))
    for produto in produtos_ordenados:
        print(produto)



def main():
    carregar_usuarios()
    carregar_produtos()

    # Criando alguns usuários e produtos de exemplo
    criar_usuario('admin', 'admin123', 'admin')
    criar_usuario('funcionario', 'func456', 'funcionario')

    criar_produto('Bola de Futebol', '001', '50.00', '100')
    criar_produto('Raquete de Tênis', '002', '150.00', '50')

    # Listando todos os produtos e usuários
    print("\nLista de Usuários:")
    listar_usuarios()
    print("\nLista de Produtos:")
    listar_produtos()

    # Atualizando um usuário e um produto
    atualizar_usuario('admin', 'newpass123', 'admin')
    atualizar_produto('002', 'Raquete de Tênis Profissional', '180.00', '30')

    # Listando produtos ordenados por nome e por preço
    print("\nProdutos ordenados por nome:")
    ordenar_produtos_por_nome()
    print("\nProdutos ordenados por preço:")
    ordenar_produtos_por_preco()

    # Buscando um produto específico
    print("\nBuscando produto por nome 'bola de futebol':")
    buscar_produto_por_nome('bola de futebol')

if __name__ == "__main__":
    main()
