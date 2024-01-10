print("""Bem vindo ao robô estrutural! Informe para ele 3 medidas de retas, ele irá
informar se o valor das 3 retas formariam um triângulo!""")
a = int(input("Reta 1: "))
b = int(input("Reta 2: "))
c = int(input("Reta 3: "))
if a+b>c and a+c>b and c+b>a:
    print("As 3 retas informadas formariam um triângulo!")
    if a == b and b == c and c == a:
        print("O triângulo formado é um EQUILÁTERO!")
    elif a == b and b != c:
        print("O triângulo formado é um ISÓSCELES!")
    elif b != a and b != c and c != a:
        print("O triângulo formado é um ESCALENO!")
else:
    print("As 3 retas informadas infelizmente não formariam um triângulo!")