#Faça um programa que leia o comprimento do cateto oposto
#e do cateto adjacente de um triângulo retângulo, calcule
#e mostre o comprimeito da hipotenusa


co = (float(input('O comprimento do cateto oposto é:')))
ca = (float(input("O comprimento do cateto adjacente é:")))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(f'A Himpotenusa vai medir {hi:.2f}:')

from math import hypot
co = (float(input('O comprimento do cateto oposto é:')))
ca = (float(input("O comprimento do cateto adjacente é:")))
hi = hypot(co, ca)
print(f'A Himpotenusa vai medir {hi:.2f}:')
