counter = 0
n = 2
while counter < 10:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            break
    else:
        print(n, end=" ")
        counter += 1
    n += 1
