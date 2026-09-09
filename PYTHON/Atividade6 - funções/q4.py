def calculadora(n1, n2, operacao):
    if operacao == 'soma': return n1 + n2
    elif operacao == 'sub': return n1 - n2
    elif operacao == 'mult': return n1 * n2
    elif operacao == 'div': return n1 / n2
    else: return 'operacao invalida'

print("CALCULADORA")
a = int(input("Insira o numero 1: "))
b = int(input("Insira o numero 2: "))
c = input("insira a operação\nOperações validas: soma, sub, mult, div")

print(f"resultado: {calculadora(a, b, c)}")