y = 0
x = 0
z = 0
while y != 999:
    y = int(input("Digite um número: ").strip())
    if y != 999:
        x += y
        z += 1
print(f"A soma dos números digitos é {x}")
print(f"A quantidade de números digitados é {z}")
