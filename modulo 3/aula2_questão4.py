def validar_ficha(classe, forca, magia):
    if classe.lower() == "guerreiro":
        return forca >= 15 and magia <= 10
    elif classe.lower() == "mago":
        return forca <= 10 and magia >= 15
    elif classe.lower() == "arqueiro":
        return 5 < forca < 15 and 5 < magia < 15
    else:
        return False

def main():
    # Solicita a classe de personagem
    classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ")

    # Solicita os pontos de força
    forca = int(input("Digite os pontos de força (de 1 a 20): "))

    # Solicita os pontos de magia
    magia = int(input("Digite os pontos de magia (de 1 a 20): "))

    # Valida a ficha do personagem
    pontos_consistentes = validar_ficha(classe, forca, magia)

    # Imprime se os pontos de atributo são consistentes com a classe escolhida
    print("Pontos de atributo consistentes com a classe escolhida:", pontos_consistentes)

if __name__ == "__main__":
    main()
 

