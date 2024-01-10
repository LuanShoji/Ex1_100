i = 0
v = 0
f = 0
c = 0
for t in range(1, 5):
    x = input("Informe seu nome: ")
    y = int(input("Informe sua idade: "))
    print("Digite:\n(1) para Masculino;\n(2) para Feminino;\n(3) para outros.")
    z = int(input("Informe seu sexo: "))
    i += y
    if y > v:
        v = y
        c = x
    if z == 2 and y < 20:
        f += 1
m = i//4
print("A média de idade das pessoas informadas foi de {} anos".format(m))
print("A pessoa mais velha é: {}".format(c))
print("O número de mulheres abaixo de 20 anos é: {}".format(f))
