produtos = ("Mouse", 170.00, "Gabinete", 250.00, "Placa Mãe", 650.00, "Cooler", 850.00, "Placa de Vídeo", 1400.00, "Monitor", 2000.00, "Teclado Mecânico", 780.00, "Headphone", 819.99, "Cadeira Gamer", 1800.00, "SSD Kingston 256GB", 620.00)
print(50*"-")
print(f'{"LISTAGEM DE PRODUTOS":^40}')
print(50*"-")
for p in range(0, len(produtos)):
    if p % 2 == 0:
        print(f"{produtos[p]:.<30}", end="")
    else:
        print(f"R$ {produtos[p]:>10}")