import csv
import pandas as pd

# Função para verificar se uma linha do CSV está malformada
def is_malformed(row):
    try:
        if len(row) != 10:
            return True
        int(row[2])  # Verifica se artist_count é um número
        int(row[3])  # Verifica se released_year é um número
        int(row[8])  # Verifica se streams é um número
        return False
    except:
        return True

# Abrir o arquivo CSV e processar os dados
file_path = 'spotify-2023.csv'

# Dicionário para armazenar a música mais tocada de cada ano
most_streamed_songs = {}

# Abrir o arquivo CSV com encoding 'latin-1'
with open(file_path, encoding='latin-1') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Pular o cabeçalho

    for row in reader:
        if is_malformed(row):
            continue  # Ignorar linhas malformadas
        
        track_name = row[0]
        artist_name = row[1]
        artist_count = int(row[2])
        released_year = int(row[3])
        streams = int(row[8])

        if 2012 <= released_year <= 2022:
            if released_year not in most_streamed_songs:
                most_streamed_songs[released_year] = [track_name, artist_name, released_year, streams]
            else:
                if streams > most_streamed_songs[released_year][3]:
                    most_streamed_songs[released_year] = [track_name, artist_name, released_year, streams]

# Criar a lista final ordenada pelos anos
most_streamed_list = [most_streamed_songs[year] for year in sorted(most_streamed_songs.keys())]

# Imprimir a lista resultante
print(most_streamed_list)
