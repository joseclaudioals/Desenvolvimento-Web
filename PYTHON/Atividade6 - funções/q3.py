def soma(n1):
    total = 0
    for i in range(1, n1+1):
        if i % 3 == 0 or i % 5 == 0:
            total = total + i

    return total

n = int(input())
print(f"A soma de todos os multiplos de 3 e 5 até {n} é {soma(n)}")