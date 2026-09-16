import requests

def chamada_api(endpoint):
    url = 'https://economia.awesomeapi.com.br/json/last/'

    resposta = requests.get(url+endpoint)
    if resposta.status_code == 200:
        dados = resposta.json()
        # pega os dicionarios internos
        # transformamos em uma lista
        # pegamos a primeira posição da lista
        dados = list(dados.values())[0]

        print(f" --- CONVERSÃO --- ")
        print(f" 1 {dados['codein']} -> {dados['bid']} {dados['code']}")

def main():
    while True:
        print('=== Cotação ===')
        print('1 - BRL / USD')
        print('2 - EUR / USD')
        print('3 - BTC / USD')
        print('4 - BTC / BRL')
        print('0 - Sair')
        opt = int(input('Escolha uma opção:'))
        match opt:
            case 1:
                endpoint = 'brl-usd'
                chamada_api(endpoint)
            case 2:
                endpoint = 'eur-usd'
                chamada_api(endpoint)
            case 3:
                endpoint = 'btc-usd'
                chamada_api(endpoint)
            case 4:
                endpoint = 'btc-brl'
                chamada_api(endpoint)
            case 0:
                break
            case _:
                print('Opção Invalida')

if __name__ == '__main__':
    main()