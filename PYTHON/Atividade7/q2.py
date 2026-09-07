import json

with  open("q2.json") as json_file:
    dados = json.load(json_file)

for produto in dados["produtos"]:
    print(f"Nome: {produto['nome']}\nCategoria: {produto['categoria']}\n Estoque: {produto['estoque']}\n Preço: {produto['preco']}\n")

for produto in dados["produtos"]:
    if produto["estoque"] < 6:
        print(f"Nome: {produto['nome']}\nCategoria: {produto['categoria']}\n Estoque: {produto['estoque']}\n Preço: {produto['preco']}\n")

valor_total = 0
maior_valor_total = [-999999999999, None]
for produto in dados["produtos"]:
    produto_valor = produto['preco'] * produto['estoque']
    print(f"Nome: {produto['nome']} - Valor total armazenado: {produto_valor}")
    valor_total += produto_valor
    if maior_valor_total[0] < produto_valor:
        maior_valor_total[0], maior_valor_total[1] = produto_valor, produto

print(f"\nProduto de maior valor no estoque")
print(f"Nome: {maior_valor_total[1]['nome']}\ncategoria: {maior_valor_total[1]['categoria']}\npreco: {maior_valor_total[1]['preco']}\nestoque: {maior_valor_total[1]['estoque']}\n")

categoria = input("Pesquise um produto por categoria: ")
for produto in dados["produtos"]:
    if produto.get("categoria") == categoria:
        print(f"Nome: {produto['nome']}\nCategoria: {produto['categoria']}\n Estoque: {produto['estoque']}\n Preço: {produto['preco']}\n")
else:
    print(f"Nenhum produto da categoria {categoria}")