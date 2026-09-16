import json

def carregar_inventario():
    try:
        with open('src/inventario.json', mode='r', encoding='utf-8') as json_file:
            return json.load(json_file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return {}

def salvar_inventario(dados):
    with open('src/inventario.json', mode='w', encoding='utf-8') as json_file:
        json.dump(dados, json_file, indent=4, ensure_ascii=False)

def adicionar_produto():
    inventario = carregar_inventario()
    while True:
        valores = input("Digite o nome e a quantidade do produto: (-1 para sair)\n: ")
        if valores == '-1':
            break

        try:
            nome, quantidade = valores.split(" ")

            chave = nome.lower().strip()
            if chave in inventario:
                inventario[chave]["quantidade"] += int(quantidade)
            else:
                inventario[chave] = {"nome": nome, "quantidade": int(quantidade)}
        except ValueError:
            print("Valores invalidos")

    salvar_inventario(inventario)

def remover_produto():
    inventario = carregar_inventario()
    chave = input("Digite o nome do produto para ser removido: \n").lower().strip()

    if chave in inventario:
        nome = inventario[chave]["nome"]
        del inventario[chave]
        salvar_inventario(inventario)
        print(f"Produto {nome} removido com sucesso!")
    else:
        print("O produto nao existe no inventario")

def listar_produtos():
    inventario = carregar_inventario()
    print("Produtos:")
    for produto in inventario.values():
        print(f"Nome: {produto["nome"]} - Quantidade: {produto["quantidade"]}")

def main():

    while True:
        print(f"-- MENU --")
        print(f"1 - Adicionar produto")
        print(f"2 - Remover produto")
        print(f"3 - Listar produtos")
        print(f"4 - Sair\n")
        opt = int(input())

        match opt:
            case 1:
                adicionar_produto()
            case 2:
                remover_produto()
            case 3:
                listar_produtos()
            case 4:
                break
            case _:
                print(f"Opcao invalida!")

    print(f"Obrigado pela confiança")

if __name__ == "__main__":
    main()