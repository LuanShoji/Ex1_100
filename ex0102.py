def fatorial(n, show=False):
     '''
     :param n: lalalalalal
     :param show: bababababab
     :return: dodododododo
     '''
     f = 1
     for n in range(n, 0, -1):
         f *= n
         if show:
            print(f"{n}", end=" x ")
     return (f'= {f}')


# Start Program
print(fatorial(5, show=True))
help(fatorial)
