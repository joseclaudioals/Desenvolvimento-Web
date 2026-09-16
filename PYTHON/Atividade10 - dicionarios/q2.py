s = ''
alunos_diario = {}
while s != 'n':
    nome = input("Qual o nome do aluno? ")
    notas = (input("Qual as nota do aluno? ").split())
    media = 0.0
    for i in range(len(notas)):
        media = media + float(notas[i])
    media = media/len(notas)

    alunos_diario[nome] = media

    s = input(f"Deseja continuar? [S/N] ").lower()

print("Diario dos alunos")
for aluno in alunos_diario:
    print(f"Nome: {aluno} | Média: {alunos_diario[aluno]}")

