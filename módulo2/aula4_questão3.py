#Leitura de dados(entrada)
produto1_nome = input("*Digite o nome do produto 1:* ")
produto1_preco_unitario = float(input("*Digite o preço unitário do produto 1:* "))
produto1_quantidade = int(input("*Digite a quantidade do produto 1:* "))

produto2_nome = input("*Digite o nome do produto 2:* ")
produto2_preco_unitario = float(input("*Digite o preço unitário do produto 2:* "))
produto2_quantidade = int(input("*Digite a quantidade do produto 2:* "))

produto3_nome = input("*Digite o nome do produto 3:* ")
produto3_preco_unitario = float(input("*Digite o preço unitário do produto 3:* "))
produto3_quantidade = int(input("*Digite a quantidade do produto 3:* "))

#Processamento
total_produto1 = produto1_preco_unitario * produto1_quantidade
total_produto2 = produto2_preco_unitario * produto2_quantidade
total_produto3 = produto3_preco_unitario * produto3_quantidade

preco_total = total_produto1 + total_produto2 + total_produto3

#impressão dos dados(saída)
print("Total: R${:,.2f}".format(preco_total))
