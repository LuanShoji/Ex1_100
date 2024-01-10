gordo = 0
magro = 0
for t in range(0, 5, 1):
    x = float(input("Informe seu peso(kg): "))
    if t == 1:
        gordo = x
        magro = x
    if x > gordo:
        gordo = x
    if x < magro:
        magro = x
print("O peso maior lido foi de {}Kg".format(gordo))
print("O peso menor lido foi de {}Kg".format(magro))








