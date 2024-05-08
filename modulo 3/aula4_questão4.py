def calcular_frete(d,p):
    if p>10:
        taxa_extra=10
    else:
        taxa_extra=0
    if d <=100:
        frete= p * 1 + taxa_extra
    if 101<=d <=300:
        frete= p * 1.5 + taxa_extra
    if d>300:
        frete= p * 2 + taxa_extra
    return frete                    
d= float(input("digite a distância do destino em km:"))
peso= p = float(input("digite o peso do objeto em kg:"))

valor_frete= vf= calcular_frete(d,p)
print("O valor do frete em R$"+ str(vf))