x = int(input("Digite um número inteiro para ser mostrada a sua tabuada: ").strip())
for t in range(0, 11, 1):
    print("{} x {} = {}".format(x, t, t*x))

