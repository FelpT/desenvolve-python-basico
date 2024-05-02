#Os códigos abaixo servem para o usuário dar entrada dos dados do problema.
comprimento= int(input("O comprimento do terreno é de:"))
largura= int(input("A largura do terreno é de:"))
preco_m2= float(input("valor do metro quadrado:"))

#calculos para descobrir o valor do terreno.
area= comprimento*largura
preco_total=pt= preco_m2*area

#Aqui é a saida dos dados aonde o código mostrará o resultado do terreno através dos dados inseridos.
print(f"O terreno possui {area} e custa {pt:,.2f}")