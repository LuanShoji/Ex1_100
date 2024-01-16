l = list()
while True:
    x = int(input("Digite um valor: "))
    l.append(x)
    c = str(input("Deseja continuar[S/N]? "))
    #while c in "":
        #print("Escolha errada, tente novamente, tecle 'S' ou 'N'!")
        #c = str(input("Deseja continuar[S/N]? "))
    if c in "Nn":
        print(f"Você digitou {len(l)} elementos!")
        l.sort(reverse=True)
        print(f"Os valores em ordem decrescente são: {l}")
        if 5 in l:
            print("O valor 5 faz parte da lista!")
        else:
            print("O valor 5 não faz parte da lista!")
        break
print("Program Finished")



