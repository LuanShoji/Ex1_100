val = list()
for v in range(0, 5):
    val.append(int(input(f"Digite o valor da posição {v}º: ")))
a = max(val)
b = min(val)
print(f"A lista criada foi: {val}")
print(f"O maior valor é {a} nas posições...", end="")
for i, c in enumerate(val):
    if c == a:
        print(f"{i}...", end="")
print()
print(f"O menor valor é {b} nas posições...", end="")
for i, c in enumerate(val):
    if c == b:
        print(f"{i}...", end="")
print()
