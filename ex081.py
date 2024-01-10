numeros = list()
val = 0
while True:
    numeros.append(int(input("Digite um valor: ")))
    val += 1
    x = input("Quer continuar?[S/N] ")
    if x in "Nn":
        break
print(f"Foram digitados {val} valores.")
print(f"Os valores em ordem descrescente são: {numeros.sort(reverse=True)}")
if 5 in numeros:
    print("O valor 5 foi encontrado na lista!")
else:
    print("O valor 5 não foi encontrado na lista!")
