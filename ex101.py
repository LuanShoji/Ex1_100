def voto(a=0):
    x = (2023 - a)
    if x < 18:
        return print(f"Com {x} anos, o seu estado é IMPOSSIBILITADO DE VOTAR")
    elif x < 65:
        return print(f"Com {x} anos, o seu estado é VOTO OBRIGATÓRIO")
    elif x > 65:
        return print(f"Com {x} anos, o seu estado é VOTO OPCIONAL")


# program start
n = int(input("Em que ano você nasceu (Ex.: 1980): "))
voto(n)
