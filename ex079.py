val = list()
o = ["S", "s", "N", "n"]
while True:
    n = int(input("Digite um valor: "))
    if n not in val:
        val.append(n)
        print("Valores adicionados!")
    else:
        print("Valores duplicados não serão adicionados!")
    a = input("Quer continuar adicionando?[S/N] ").upper()
    while a not in o:
        print("Opção incorreta!")
        a = input("Quer continuar adicionando?[S/N] ").upper()
    if a == "N":
        break
val.sort()
print(f"Os valores adicionados foram: {val}")
