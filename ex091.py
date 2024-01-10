from time import sleep
import random
desafio = list()
resultados = dict()
input(" ")
x = 1
y = 0
a = [0, 1, 2, 3, 4, 5, 6]
for z in range(0, 4, 1):
    resultados['Jogador 1'] = f'{x}'
    resultados['Dados'] = random.choice(a)
    x += 1
    desafio.append(resultados.copy())
for i in desafio:
    for x in i.i():
        print(x)






