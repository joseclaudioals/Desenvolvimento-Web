n = []
maximo = -9999999999
for i in range(10):
    n.append(int(input()))
    if n[i]%2 == 0 and n[i]>maximo:
        maximo = n[i]

print(f"Maior numero par: {maximo}")

