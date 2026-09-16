def descobrir_signo(dia, mes):
    signos_datas = {
        "Aquário": {"inicio": (1, 20), "fim": (2, 18)},
        "Peixes": {"inicio": (2, 19), "fim": (3, 20)},
        "Áries": {"inicio": (3, 21), "fim": (4, 19)},
        "Touro": {"inicio": (4, 20), "fim": (5, 20)},
        "Gêmeos": {"inicio": (5, 21), "fim": (6, 20)},
        "Câncer": {"inicio": (6, 21), "fim": (7, 22)},
        "Leão": {"inicio": (7, 23), "fim": (8, 22)},
        "Virgem": {"inicio": (8, 23), "fim": (9, 22)},
        "Libra": {"inicio": (9, 23), "fim": (10, 22)},
        "Escorpião": {"inicio": (10, 23), "fim": (11, 21)},
        "Sagitário": {"inicio": (11, 22), "fim": (12, 21)},
        "Capricórnio": {"inicio": (12, 22), "fim": (1, 19)}
    }


    data =(mes, dia)
    for signo, periodo in signos_datas.items():
        inicio = periodo["inicio"]
        fim = periodo["fim"]
        if inicio < fim:
            if inicio <= data <= fim:
                return signo
        else:
            if inicio >= data <= fim:
                return signo

    return 'Data invalida'

def main():
    dia, mes, _ = input("Digite sua data de nascimento: (Formato: dd/mm/aaaa sem as barras) ").split()
    print(f'Seu signo é: {descobrir_signo(int(dia), int(mes))}')

if __name__ == '__main__':
    main()