s, n1, n2 = input("Coloque o nome do aluno e duas notas (separe por espaço):\n").split()
print(f"Aluno: {s}\nMaior nota {n1 if float(n1) > float(n2) else n2}")