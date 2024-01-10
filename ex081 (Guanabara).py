valores = []
while True:
    valores.append(int(input("Digite um valor: ")))
    resp = str(input("Quer continuar? [S/N]  "))
    if resp in "Nn":
        break
print("-=" * 30)
print(f"Você digitou {len(valores)} elementos.")
valores.sort()
print(f"Os valors em ordem decrescente são {valores}")