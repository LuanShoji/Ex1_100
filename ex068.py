from time import sleep
import random
print("Robot Le: Vamos jogar ímpar ou par!")
n = str(input("Qual seu nome jogador? ")).strip()
print(f"Você escolhe primeiro {n}!")
print("[1] Ímpar\n[2] Par")
v = 0
while True:
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    x = int(input("Sua escolha: "))
    if x != 1 and x != 2:
        print("Escolha incorreta, selecione a opção citada anteriormente! [1] Ímpar ou [2] Par.")
        while x != 1 and x != 2:
            x = int(input("Sua escolha: "))
    y = int(input("Escolha um número de 0 a 10: "))
    r = random.choice(a)
    j = y + r
    if x == 1:
        print(f"Jogador {n} escolheu ÍMPAR!")
        print(f"Robot Le ficou com PAR!")
        print("1")
        sleep(1)
        print("2")
        sleep(1)
        print("3.... E JÁ!")
        if j % 2 != 0:
            print(f"PARABÉNS {n}!\nVocê conseguiu vencer o Robot Le.")
            print(f"Você jogou {y} e o Robot Le {r}, resultando em {y + r}")
            v += 1
        else:
            print(f"QUE PENA {n}!\nVocê não conseguiu vencê-lo.")
            print(f"Você jogou {y} e o Robot Le {r}, resultando em {y + r}")
            break
    elif x == 2:
        print(f"Jogador {n} escolheu PAR!")
        print(f"Robot Le ficou com ÍMPAR!")
        print("1")
        sleep(1)
        print("2")
        sleep(1)
        print("3......... E JÁ!")
        if j % 2 == 0:
            print(f"PARABÉNS {n}!\nVocê conseguiu vencer o Robot Le.")
            print(f"Você jogou {y} e o Robot Le {r}, resultando em {y + r}")
            v += 1
        else:
            print(f"QUE PENA {n}!\nVocê não conseguiu vencê-lo.")
            print(f"Você jogou {y} e o Robot Le {r}, resultando em {y + r}")
            break
print(f"O número de vitórias concecutivas foi de {v}")
print("FIM DE JOGO!")
