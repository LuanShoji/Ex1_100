from time import sleep
print("BEM VINDO AO BANCO CENTER!")
x = int(input("Informe o valor do saque: "))
s = x
c = 50
q = 0
a = 0
b = 0
d = 0
while True:
    if s >= c:
        s -= c
        q += 1
    else:
        c = 20
        if s >= c:
            s -= c
            a += 1
        c = 10
        if s >= c:
            s -= c
            b += 1
        c = 5
        if s >= c:
            s -= c
            d += 1
        if s == 0:
            break
print("Separando cédulas...")
sleep(2)
if q != 0:
    print(f"{q} cédulas de 50 reais.")
if a != 0:
    print(f"{a} cédulas de 20 reais")
if b != 0:
    print(f"{b} cédulas de 10 reais.")
if d != 0:
    print(f"{d} cédulas de 5 reais.")
print("VOLTE SEMPRE!")

