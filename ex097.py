def escreva(a):
    c = len(a) + 4
    print(c * "-")
    print(f"  {a}")
    print(c * "-")


#start program
a = str(input("Escreva um texto: "))
escreva(a)
