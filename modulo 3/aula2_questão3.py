#entrada de dados
idade= int(input())
quantas_vezes_jogou=games= int(input())
quantas_vezes_venceu=wins= int(input())
#processamento
Adimitido=(16<=idade<=18)and (games>=3) and (wins>=1)
#saida
print(f"Apto para ingressar no clube de jogos de tabuleiro:",Adimitido)