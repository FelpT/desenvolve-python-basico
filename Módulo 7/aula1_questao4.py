def formatar_numero(numero):
   
    if len(numero) == 8:
        numero = '9' + numero
    elif len(numero) == 9 and numero[0] != '9':
        return "Número inválido. O primeiro dígito deve ser 9 para números de 9 dígitos."

   
    numero_formatado = numero[:5] + '-' + numero[5:]
    
    return f"Número completo: {numero_formatado}"

numero = input("Digite o número: ")
resultado = formatar_numero(numero)
print(resultado)
