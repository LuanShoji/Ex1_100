a1 = int(input("Informe o primeiro termo da progressão: "))
r = int(input("Informe a razão(nº de sequências) a ser calculada: "))
décimo = a1 + (10 - 1)*r
for a in range(a1, décimo+1, r):
    print("{}".format(a))
