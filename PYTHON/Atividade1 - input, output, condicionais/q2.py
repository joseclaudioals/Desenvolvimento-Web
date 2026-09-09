n = int(input("Insira um numero inteiro: "))

isPrime = True

if n<=1:
    isPrime = False

for i in range(2,int(n**0.5)+1):
    if n%i==0:
        isPrime = False
        break

if isPrime:
    print("O numero é primo")
else:
    print("O numero não é primo")

