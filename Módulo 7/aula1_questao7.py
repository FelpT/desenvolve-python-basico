import random

def encrypt(nomes):

    n = random.randint(1, 10)
    
   
    def encrypt_char(c, n):
        new_char = ord(c) + n
        if new_char > 126:
            new_char = 33 + (new_char - 127)
        return chr(new_char)
    

    nomes_cript = []
    for nome in nomes:
        nome_cript = ''.join(encrypt_char(c, n) for c in nome)
        nomes_cript.append(nome_cript)
    
    return nomes_cript, n


nomes = ["Filipe", "Vicente", "Julia", "Cristina", "Nazaré", "Maria"]
nomes_cript, chave_aleatoria = encrypt(nomes)
print(f"Chave aleatória: {chave_aleatoria}")
print(f"Nomes criptografados: {nomes_cript}")
