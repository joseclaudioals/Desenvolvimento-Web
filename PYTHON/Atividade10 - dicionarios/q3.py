carrinho = {}
s = ''
while s != 'n':
    nome_produto = input('Digite o nome do produto: ')
    qnt = int(input('Digite a quantidade de produto: '))

    carrinho[nome_produto] = qnt

    s = input(f'Deseja continuar? [S/N]').lower()

print(" - Items no carrinho - ")
for produto in carrinho:
    print(f'Nome do produto: {produto} | Quantidade: {carrinho[produto]}')