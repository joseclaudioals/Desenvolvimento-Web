lista = {}
s = ''
while s != 'n':
    convidado = input("Insira o nome do convidado: ")
    if convidado in lista:
        lista[convidado] += 1
    else:
        lista[convidado] = 1

    s = input(f'Deseja continuar? [S/N]').lower()

for convidado, qtd in lista.items():
    print(f' Nome do Convidado: {convidado} | Recorrencia na lista: {qtd}')