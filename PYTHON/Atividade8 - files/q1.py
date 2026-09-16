import csv

media = 0.00
qnt = 0

with open('src/produtos.csv', mode ='w', encoding='utf-8', newline='') as produtos:
    writer = csv.DictWriter(produtos, fieldnames=['nome', 'preco'])
    writer.writeheader()

    while True:
        valores = input(f"Insira o nome e o preço separados por espaço\nPara terminar os inputs, digite '-1'\n").strip()
        if valores == '-1':
            break
        try:
            nome, preco = valores.split(' ')
            writer.writerow({'nome': nome, 'preco': preco})
        except ValueError:
            print(f"Valores invalidos")

with open('src/produtos.csv', mode='r', encoding='utf-8', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for produto in reader:
        qnt+=1
        print(f"Produto: {produto['nome']} | Preço: {produto['preco']}")
        media += float(produto['preco'])


if qnt > 0:
    media = media / qnt
    print(f"Media: {media:.2f}")
else: print("Csv vazio")