'''import math
a = float(input('Digite um número flutuante:'))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(a, math.trunc(a)))
print('Arredondando para mais, seu número fica como {}'.format(math.ceil(a)))
print('Arredondando para menos, ficará como {}'.format(math.floor(a)))'''

from math import ceil, floor
n = float(input("digite um número flutuante"))
i = int(n)
c = ceil(n)
f = floor(n)
print(f"O número flutuante {n} se torna {i}")
print(f"Seu arreondamento para cima é {c}")
print(f"E seu arrendondamento para baixo, é {f}")