y = 0
m = 0
a = 0
z = 99999**99999
while True:
    x = int(input("Digite um número: "))
    print("Você quer continuar?")
    p = int(input("[1] - SIM / [2] - NÃO: "))
    if x > y:
        y = x
    if x < z:
        z = x
    m += x
    a += 1
    if p == 2:
        break
print(f"A média entre os valores digitados é {m/a:.2f}")
print(f"O maior valor digitado é {y}")
print(f"O menor valor digitado é {z}")