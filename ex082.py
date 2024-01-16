g = list()
i = list()
p = list()
while True:
    x = int(input("Digite um valor: "))
    g.append(x)
    if x % 2 == 0:
        p.append(x)
    else:
        i.append(x)
    c = str(input("Deseja continuar [S/N]? "))
    if c in "Nn":
        break
print(f"Os número digitados foram {g}")
print(f"Os números ímpares digitados foram {i}")
print(f"Os números pares digitados foram {p}")
print("END")
