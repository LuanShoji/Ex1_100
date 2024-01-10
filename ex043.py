x = float(input("Informe o seu peso(kg): ").strip())
y = float(input("Informe sua altura(m): ").strip())
a = float(x/(y**2))
if a < 18.5:
    print("Abaixo do peso!")
elif a >= 18.5 and a < 25:
    print("Peso ideal!")
elif a >= 25 and a < 30:
    print("Sobrepeso!")
elif a >= 30 and a < 40:
    print("Obesidade!")
elif a >= 40:
    print("Obesidade mórbida!")