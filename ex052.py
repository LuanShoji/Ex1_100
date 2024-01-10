x = int(input("Informe um valor: "))
if x % 2 != 0 or x <= 3:
    print("O número {} informado é um número primo!".format(x))
else:
    print("O número {} informado não é um número primo!".format(x))
