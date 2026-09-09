print("Cadastro")
nome = input("Qual o seu nome? ")
idade = int(input("Qual a sua idade? "))
altura = float(input("Qual a sua altura? "))
estudante = True

hobbies = []
s = ''
while s.lower() != "n":
    hobbies.append(input("Qual a hobbie?"))
    s = input("Deseja adicionar? [S/N]")

print(f"Nome{nome}")
print(f"Idade{idade}")
print(f"Altura{altura}")
print(f"Estudante{estudante}")
print(f"Cargo: { estudante if "estudante" else  "nao estudante"}")
print(f"Hobbies: ", end="")
for hobbie in hobbies:
    print(f" {hobbie} | ", end="")