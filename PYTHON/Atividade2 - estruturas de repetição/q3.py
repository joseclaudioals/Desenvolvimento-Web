def raiz(n):
    if n < 0:
        return "Nao existe raiz real para numeros negativos"
    if n == 0:
        return 0

    chute = n / 2.0
    margem = 0.0001

    while abs((chute ** 2) - n) > margem:
        chute = (chute + (n / chute)) / 2.0

    return chute

n = int(input("Insira um numero inteiro: "))
raiz = (raiz(n))
print(f"A raiz quadrada aproximada do numero {n} é {raiz:.4f}")