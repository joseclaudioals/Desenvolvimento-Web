import random
import json
import os

alunos = []

if not os.path.exists("src/banco.json"):
    alunos = []
with open("src/banco.json", "r", encoding="utf-8") as arquivo:
    try:
        alunos = json.load(arquivo)
    except json.JSONDecodeError:
        alunos = []
if not alunos:
    alunos = []

while True:
    nome = input(f"Digite o nome do aluno ou -1 para sair: ")

    if nome == "-1":
        break

    alunos.append(nome)

while True:
    qnt_sorteios = int(input(f"Digite quantos sorteios deseja sair? "))
    if qnt_sorteios <= 0:
        print("A quantidade de sorteios deve ser maior que zero")
        continue
    elif qnt_sorteios >= len(alunos):
        print("A quantidade de sorteios deve ser menor que a quantidade de alunos")
        continue
    else:
        break


for i in range(qnt_sorteios):
    print("embaralhando alunos")
    random.shuffle(alunos)
    aluno_sorteado = random.randint(1, len(alunos) + 1)
    print(f"o aluno sorteado foi: {alunos[aluno_sorteado]}")

with open("src/banco.json", "w", encoding="utf-8") as arquivo:
    json.dump(alunos, arquivo, indent=4, ensure_ascii=False)

