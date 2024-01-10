from random import randint
from time import sleep
from operator import itemgetter
input()
desafio = {'Jogador 1': randint(0, 6),
           'Jogador 2': randint(0, 6),
           'Jogador 3': randint(0, 6),
           'Jogador 4': randint(0, 6)}
ranking = dict()
for i, k in desafio.items():
    sleep(1)
    print(f"O {i} tirou o valor {k} no dado!")
ranking = sorted(desafio.items(), key=itemgetter(1), reverse=True)
print(ranking)
#devido ao ranking virar uma lista
for i, v in enumerate(ranking):
    print(f"{i}º Lugar: {v[0]} que tirou {v[1]} no dado")
