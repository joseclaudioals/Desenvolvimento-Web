def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3)/3

print(f"media: {calcular_media(*map(int, input().split()))}")