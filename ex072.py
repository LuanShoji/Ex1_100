n = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")
x = int(input("Digite um número de 0 a 20: "))
while x < 0 or x > 20:
    x = int(input("Número incorreto, digite novamente um número de 0 a 20: "))
print(f"Você digitou {n[x]}")
