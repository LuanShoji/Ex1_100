def contador():
    for c in range(0, 11, 1):
        print(c, end=" ")
    print("(Fim da primeira contagem!)\n")
    for c in range(10, 0, -2):
        print(c, end=" ")
    print("(Fim da segunda contagem!)\n")
    print("Agora é sua vez de personalizar!")
    a = int(input("Início: "))
    b = int(input("Fim: "))
    d = int(input("Intervalo: "))
    if d < 0:
        d = d - d - d
        if a > b:
            for c in range(a, b, -d):
                print(c, end=" ")
        else:
            for c in range(a, b, d):
                print(c, end=" ")
    elif d == 0:
        d = 1
        if a > b:
            for c in range(a, b, -d):
                print(c, end=" ")
        else:
            for c in range(a, b, d):
                print(c, end=" ")
    elif a > b:
        for c in range(a, b, -d):
            print(c, end=" ")
    else:
        for c in range(a, b, d):
            print(c, end=" ")


# start
print("Início do programa!")
contador()
