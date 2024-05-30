def substituir_vogais(frase):
    vogais = "aeiouAEIOU"
    frase_modificada = ""
    for caractere in frase:
        if caractere in vogais:
            frase_modificada += "*"
        else:
            frase_modificada += caractere
    return frase_modificada

frase = input("Digite uma frase: ")
frase_modificada = substituir_vogais(frase)

print(f"Frase modificada: {frase_modificada}")
