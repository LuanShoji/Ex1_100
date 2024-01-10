x = str(input("Digite uma frase que te motive: ")).strip()
print("O número de caractéres (a) é de {}".format(x.upper().count("A")))
print("A posição que ela aparece pela primeira vez é a {}".format(x.upper().find("A")))
print("A posição que ela aparece pela última vez é a {}".format(x.upper().rfind("A")))
