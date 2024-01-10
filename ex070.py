k = 0
c = 0
q = 9**99999
n = 0
print("BEM VINDOOOOOOOOOOO AO MERCADÃOOOOOOOOOOOOOOOOOOO!!!")
while True:
    x = input("Informe o nome do produto: ")
    y = float(input("Custo(R$): "))
    c += y
    if y >= 1000:
        k += 1
    elif y < q:
        q = y
        n = x
    z = input("Deseja continuar[S / N]? R: ").upper()
    if z == "N":
        break
print("TOTAL(R$): {:.2f}".format(c))
print(f"{k} são produtos acima de R$1000,00!!")
print(f"O produto mais barato passado foi {n}!")