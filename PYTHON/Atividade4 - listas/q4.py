n = []

while True:
    i = int(input())
    if i == -1:
        break
    n.append(int(i))

n.sort(reverse=True)

for i in n:
    if i % 2 == 0: print(i)
