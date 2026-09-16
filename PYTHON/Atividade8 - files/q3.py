import datetime as dt

def contar_palavras():
    total_palavras = 0
    with open('src/diario.txt', mode='r', encoding='utf-8') as arquivo:
        for linha in arquivo :
            total_palavras += len(linha.split())

    return total_palavras

def marcar_arquivo():
    data_hoje = dt.datetime.now()
    with open('src/diario.txt', mode='a', encoding='utf-8') as arquivo:
        arquivo.write(str(f"\nData hoje: {data_hoje} | Total de palavras: {contar_palavras()}\n"))

def mostrar_arquivos():
    with open('src/diario.txt', mode='r', encoding='utf-8') as arquivo:
        for linha in arquivo :
            print(linha)

def main():
    print(f"Quantidade de palavras no diário: {contar_palavras()}")
    mostrar_arquivos()
    marcar_arquivo()
    mostrar_arquivos()

if __name__ == "__main__":
    main()