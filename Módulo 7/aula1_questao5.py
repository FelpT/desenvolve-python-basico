frase= str(input("Digite uma frase:"))
cont_vogais=0
indices=[]
for i in range(len (frase)):
    if frase[i] in "aeiouAEIOU":
        cont_vogais+=1
        indices.append(i)
print(cont_vogais)
print(indices)