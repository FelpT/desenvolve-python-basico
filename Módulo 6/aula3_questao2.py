# Lista de URLs
urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

# Lista para armazenar os domínios
dominios = []

# Itera sobre cada URL na lista
for url in urls:
    # Remove "www." do início e ".com" do final, e adiciona o resultado à lista de domínios
    dominio = url[4:-4]
    dominios.append(dominio)

# Imprime a lista de domínios
print("Domínios:", dominios)
