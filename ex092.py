from time import sleep
ctps = dict()
ctps['Nome'] = str(input("Informe seu nome: "))
x = int(input("Informe o ano de nascimento: "))
ctps['Idade'] = 2022-x
ctps['Carteira'] = int(input('Informe a numeração da sua carteira de trabalho (digite [0] se não tiver): '))
if ctps['Carteira'] == 0:
    for k, v in ctps.items():
        print(f"{k} tem o valor {v}")
        sleep(1)
else:
    ctps['Contratação'] = int(input("Informe o ano de contratação: "))
    ctps['Salário'] = float(input("Informe seu salário: "))
    y = 35 + ctps['Contratação']
    ctps['Aposentadoria'] = y - x
    for z, w in ctps.items():
        print(f"{z} tem o valor {w}")
        sleep(1)
