def calcular_digito(cpf, posicoes):
    soma = sum(int(cpf[i]) * (posicoes - i) for i in range(posicoes - 1))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

def validar_cpf(cpf):
  
    cpf = cpf.replace(".", "").replace("-", "")
    
    if len(cpf) != 11 or not cpf.isdigit():
        return False

    
    primeiro_digito = calcular_digito(cpf, 10)
    
    
    segundo_digito = calcular_digito(cpf + str(primeiro_digito), 11)
    
    
    return cpf[-2:] == f"{primeiro_digito}{segundo_digito}"


cpf_usuario = input("Digite seu CPF (XXX.XXX.XXX-XX): ")

if validar_cpf(cpf_usuario):
    print("Válido")
else:
    print("Inválido")
