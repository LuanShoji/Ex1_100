print("Informe o valor para ser descoberto seu fatorial!")
x = float(input("Informe o valor: "))
a = 1
while x != 1:
    a *= x
    x -= 1
print("O fatorial do valor informado é {}".format(a))
