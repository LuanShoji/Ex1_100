y = list()
x = str(input("Digite uma expressão numérica: "))
for c in x:
    y.append(c)
a = y.count('(')
b = y.count(')')
if a == b:
    print("Sua expressão númerica está correta!")
else:
    print("Sua expressão númerica está incorreta! Tente novamente!")