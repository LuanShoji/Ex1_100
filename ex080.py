val = list()
for c in range(0, 5):
    a = int(input("Digite um valor: "))
    if c == 0:
        val.append(a)
    elif a < val[0]:
        val.insert(0, a)
    elif a > val[0]:
        val.append(a)
    elif a > val[1]:
        val.insert(1, a)
print(val)
