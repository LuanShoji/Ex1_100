numeros = [[], []]
x = 0
for n in range(0, 7, 1):
    x = int(input("Digite um número: "))
    if x % 2 == 0:
        numeros[0].append(x)
    else:
        numeros[1].append(x)
numeros[0].sort()
numeros[1].sort()
print(numeros)
