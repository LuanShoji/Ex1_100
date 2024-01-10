from random import randint
numeros = list()


def sorteio():
    for c in range(0, 5):
        numeros.append(randint(0, 100))
    print(f"Os números sorteados são {numeros}")


def somaPar():
    p = 0
    for c in numeros:
        if c % 2 == 0:
            p += c
    print(f"A soma dos números pares se resulta em {p}")

sorteio()
somaPar()