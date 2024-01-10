from time import sleep
p = 0
s = 1
M = 0
print("Informe valores a serem utilizados em operações matemáticas")
x = float(input("Digite um número: "))
y = float(input("Digite um número: "))
print("OPÇÕES:\n[1] - Somar;\n[2] - Multiplicar;\n[3] - Maior;\n[4] - Novos números;\n[5] - Sair do programa.")
a = int(input("Escolha a opção desejada: "))
while a != 1 and a != 2 and a!= 3 and a != 4 and a!= 5:
    print("Opção incorreta, favor selecionar as opções citadas acima!")
    a = int(input("Escolha a opção desejada: "))
while a == 4:
    z1 = float(input("Digite um número: "))
    p += z1
    s *= z1
    if z1 > M:
        M = z1
    a = int(input("Escolha a opção de operação desejada: "))
if a == 1:
    z = x + y + p
    print("A soma dos valores informados foi de {}".format(z))
elif a == 2:
    m = x * y * s
    print("A multiplicação dos valores informados foi de {}".format(m))
elif a == 3:
    if x > y:
        if x > M:
            print("O maior valor é {}".format(x))
        else:
            print("O maior valor é {}".format(M))
    elif y > M:
        print("O maior valor é {}".format(y))
    else:
        print("O maior valor é {}".format(M))
elif a == 5:
    print("Saindo do programa...")
    sleep(1.5)
    print("Programa fechado!")