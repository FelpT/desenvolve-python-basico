alunos = ["Maria", "Jose", "Carla", "Sol"]
notas = [35, 50, 20, 80]
aprovados=[alunos[i] if notas[i] >=60 else "Reprovado" for i in range(len(alunos))]
print(aprovados)