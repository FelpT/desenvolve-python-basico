a= int(input("Digite algum ano(Ex:1986)"))
if a%4 == 0 and a%100 > 0 or a%400 == 0:
    print("Bissexto")
else:
    print("Não é bissexto")    