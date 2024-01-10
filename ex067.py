x = 1
while x > 0:
    x = int(input("Digite o número que você quer a tabuada: "))
    if x < 0:
        break
    for t in range(0, 11, 1):
        print(f"{x} x {t} = {x*t}")
print("PROGRAMA TABUADA ENCERRADO!")