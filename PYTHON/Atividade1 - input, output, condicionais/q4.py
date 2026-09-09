n = int(input("Insira um numero inteiro: "))

total = 0

for i in range(1,n):
    if n % i == 0:
        total += i

if total == n:
    print("O numero é perfeito")
else:
    print("O numero nao é perfeito")