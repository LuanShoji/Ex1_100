t = ('Palmeiras', 'Internacional', 'Flamengo', 'Fluminense', 'Corinthians', 'Athletico-PR', 'Atlético-MG', 'América-MG', 'Goiás', 'Santos', 'Bragantino', 'Botafogo', 'São Paulo', 'Ceará', 'Fortaleza', 'Coritiba', 'Cuiabá', 'Avaí', 'Atletico-GO', ' Juventude')
x = sorted(t)
c = t.index("Cuiabá")
print(f"Os 5 primeiros colocados são {t[:5]}")
print(f"Os últimos colocados da tabela são {t[-4:]}")
print(f"Os times em ordem alfabética {x}")
print(f"O time Cuiabá está em {c+1}º lugar")