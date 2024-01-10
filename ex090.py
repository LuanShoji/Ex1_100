boletim = dict()
boletim["aluno"] = str(input("Aluno(a): "))
boletim["Media"] = float(input("Média: "))
if boletim['Media'] < 6:
    boletim["situacao"] = "Reprovado"
else:
    boletim["situacao"] = "Aprovado"
print(f"O(a) Aluno(a) {boletim['aluno']}")
print(f"Ficou com a média {boletim['Media']}")
print(f"Situação: {boletim['situacao']}")
