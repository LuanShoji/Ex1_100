x = int(input("Digite um número (0 a 9): "))
y = int(input("Digite um número (0 a 9): "))
z = int(input("Digite um número (0 a 9): "))
w = int(input("Digite um número (0 a 9): "))
a = (x, y, z, w)
c = 0
print(f"O número 9 apareceu {a.count(9)} vezes!")
if 3 in a:
    print(f"O número 3 foi digitado na {a.index(3)+1}º posição!")
else:
    print(f"Não foi digitado nenhuma vez o número 3!")
print("Os números pares digitados são: ")
for c in range(0, 4):
    b = (a[c])
    if b % 2 == 0:
        print(f"{b}")
print("FIM")
