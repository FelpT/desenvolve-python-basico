n1= float(input("Digite um valor x:"))
n2= float(input("Digite um valor y:"))

diferença_absoluta= abs(n1-n2)
diferença_arredondada= round(diferença_absoluta, 2)

print(f"A diferença absoluta entre os dois números é:{diferença_arredondada:.2f}")