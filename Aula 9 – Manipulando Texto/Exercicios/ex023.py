"""Faça um programa que leia um número de 0 a 9999 e mostre na tela
cada um dos digitos separados

EX:

Digite um número= 1997

Unidade=7
Dezena=9
Centena=9
Milhar=1   """

data = (input('Insira sua data de nascimento'))
u = data[3:]
d = data[2:3]
c = data[1:2]
m = data[:1]

print(f'UNIDADE:{u}')
print(f'DEZENA:{d}')
print(f'CENTENA:{c}')
print(f'MILHAR:{m}')


#Meneira Matemática
dat = int(input('Digite a data de Nascimento'))
print(f'ANALIZANDO ANO DE: {dat}')

un = dat // 1 % 10
de = dat // 10 % 10
ce = dat // 100 % 10
mi = dat // 1000 % 10

print(f'Unidade:{un}')
print(f'Dezena:{de}')
print(f'Centena:{ce}')
print(f'Milhar:{mi}')