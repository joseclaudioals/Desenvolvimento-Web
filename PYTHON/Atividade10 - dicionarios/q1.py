frase = "que a força esteja com você"
palavras = frase.lower().split()

frequencia = {}
for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1

for palavra in frequencia:
    print(f"{palavra}: {frequencia[palavra]}")