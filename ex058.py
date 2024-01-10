import random
nome = str(input("Você é aquele cara do desafio 28 né? Esqueci o seu nome, podes repetir? ")).strip()
print("""Olá novamente {}, você está aqui para ser testado, novamente sua vida e de várias outras pessoas está entre a vida e a morte, você
terá que advinhar um número de 0 a 10 que o robô irá escolher, se acertar irei poupar sua vida e a das pessoas no mundo, se errar... você terá
várias tentativas, mas cada erro é uma vida no mundo a menos, tente acertar de primeira!""".format(nome))
n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
robo = random.choice(n)
y = int(input("Qual o valor que o robô escolheu? "))
c = 0
while y != robo:
    print("Menos uma pessoa no mundo...")
    y = int(input("Qual o valor que o robô escolheu?: "))
    c += 1
print("Omedetouuuuu, você conseguiu descobrir, você poderá prosseguir com sua vidinha {}".format(nome))
if c == 0:
    print("Uau, você é bom mesmo!")
else:
    print("O número de pessoas mortas devido suas tentativas foi de {}".format(c))

