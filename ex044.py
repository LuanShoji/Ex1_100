x = float(input("Informe o total a ser pago: ").strip())
print("Formas de pagamento:\n1 - À vista dinheiro/cheque;\n2 - À vista no cartão;\n3 - Em até 2x no cartão;\n4 - 3x ou mais no cartão.")
y = int(input("Forma de pagamento: "))
if y == 1:
    a = (x*0.1)
    print("O valor a ser pago será de R${}.".format(x-a))
elif y == 2:
    b = (x*0.05)
    print("O valor a ser pago será de R${}".format(x-b))
elif y == 3:
    print("O valor a ser pago será de R${}".format(x))
elif y == 4:
    c = (x*0.2)
    print("O valor a ser pego será de prestações de 3x de R${:.2f} ".format((x+c)/3))
