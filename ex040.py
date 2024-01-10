x = float(input("AV1: "))
y = float(input("AV2: "))
z = ((x+y)/2)
if z < 5.0:
    print("Aluno reprovado!\n\nBOAS FESTAS!")
elif z >= 5.0 and z <= 6.9:
    print("Aluno deverá fazer recuperação!")
elif z > 7.0:
    print("Aluno aprovado!\n\nBOAS FESTAS!")