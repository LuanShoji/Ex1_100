x = int(input("Quantos termos você quer mostrar? "))
y = 0
z = 0
w = 1
while x != 0:
     y = z + w
     z = w
     w = y
     x -= 1
     print(y)