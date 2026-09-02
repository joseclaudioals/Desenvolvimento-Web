n = int(input())
for i in range(1, n+1):
    print("".join(map(str, range(1, i+1))))
for i in range(n, 0, -1):
    print("".join(map(str, range(1, i+1))))