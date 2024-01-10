n = 0
c = 0
y = 0
while n != 999:
    n = int(input("Digite um número: "))
    c += 1
    if n == 999:
        break
    y += n
print(f"A soma dos {c} valores é {y}")
