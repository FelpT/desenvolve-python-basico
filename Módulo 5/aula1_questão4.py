import locale
from datetime import datetime

locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')

data_hora_atual = datetime.now()

data_hora_formatada = data_hora_atual.strftime("%A, %d de %B de %Y %H:%M:%S")

print(f"Data e hora atuais: {data_hora_formatada}")
