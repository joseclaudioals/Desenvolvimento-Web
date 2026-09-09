n = []
opt = 0
while True:
    opt = int(input())
    if opt == -1: break
    n.append(opt)

vistos = []
repetidos = []

for numero in n:
    if numero in vistos:
        repetidos.append(numero)
    else:
        vistos.append(numero)

print(repetidos)