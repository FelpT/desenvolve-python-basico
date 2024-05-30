# Função para converter mês numérico para nome por extenso
def mes_por_extenso(mes):
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    return meses[mes - 1]

data_nascimento = input("Digite uma data de nascimento (dd/mm/aaaa): ")
dia, mes, ano = data_nascimento.split('/')
mes = int(mes)
nome_mes = mes_por_extenso(mes)

print(f"Você nasceu em {dia} de {nome_mes} de {ano}.")
