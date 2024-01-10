m = 0
h = 0
p = 0
while True:
    y = input("Informe seu nome: ")
    z = int(input("Informe sua idade: "))
    if z > 18:
        p += 1
    print("[1]: Masculino;\n[2]: Feminino.")
    a = int(input("Informe seu sexo: "))
    if a == 2 and z < 20:
        m += 1
    elif a == 1:
        h += 1
    print("Cadastrada com sucesso! Deseja continuar fazer um novo cadastro? ")
    w = int(input("[1]: Sim;\n[2]: Não.\nR: "))
    if w == 2:
        break
print(f"São {p} que são maiores de idade!")
print(f"Foram cadastrados {h} homens!")
print(f"São {m} pessoas do sexo feminino que tem abaixo de 20 anos!")