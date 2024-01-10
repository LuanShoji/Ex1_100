def maior(l):
    print(f"Os números informados são {a}")
    print(f"O maior número informado foi: {max(l)}")


a = list()
# start
while True:
    a.append(int(input("Informe um número: ")))
    e = str(input("Deseja continuar? [S/N] "))
    if e in "Nn":
        break
maior(a)