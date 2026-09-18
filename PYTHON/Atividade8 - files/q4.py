acessos = 0
with open('src/acessos.txt', mode='w', encoding='utf-8') as arquivo:
    arquivo.write(f"{acessos}")

while True:
    print("Acessar arquivo - 1")
    print("Sair ------------ 0")
    opt = int(input())

    match opt:
        case 1:
            acessos += 1
            with open('src/acessos.txt', mode='w', encoding='utf-8') as arquivo:
                arquivo.write(f"{acessos}")
            print("Arquivo acessado com sucesso")
        case 0:
            print(f"Quantidade de acessos no arquivo: {acessos}")
            break
        case _:
            print("Opção invalida")