pessoas = list()
temp = list()
cont = 0
while True:
    temp.append(str(input("Informe seu nome: ")))
    temp.append(float(input("Informe sua massa corporal (kg): ")))
    pessoas.append(temp[:])
    temp.clear()
    cont += 1
    a = str(input("Deseja continuar? [S/N] ").upper())
    if a == "N":
        break
y = list()
z = list()
x = 0
for p in pessoas:
    if x == 0:
        y.append(p[:])
        z.append(p[:])
    x += 1
    if (y[0][1]) < p[1]:
        (y[0][1]) = p[1]
        (y[0][0]) = p[0]
    if p[1] < (z[0][1]):
        (z[0][1]) = p[1]
        (z[0][0]) = p[0]
print(f"O número de pessoas registradas foi de {cont}")
print(f"A maior pesagem foi de {y[0][1]} registrado em nome de {y[0][0]}")
print(f"A menor pesagem foi de {z[0][1]} registrado em nome de {z[0][0]}")
