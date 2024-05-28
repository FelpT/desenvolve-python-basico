frase = input("Digite uma frase: ")
vogais, consoantes = sorted([letra.lower() for letra in frase if letra.lower() in 'aeiou']), [letra for letra in frase if letra.isalpha() and letra.lower() not in 'aeiou']

print("Vogais:", vogais)
print("Consoantes:", consoantes)
