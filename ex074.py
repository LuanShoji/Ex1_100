import random
x = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
c = 0
z = 0
p = 9*999
print("Valores sorteados: ")
for c in range(0,5,1):
    y = random.choice(x)
    print(f'{y}')
    if y > z:
        z = y
    elif y < p:
        p = y
print(f"O maior valor é {z}")
print(f"O menor valor é {p}")