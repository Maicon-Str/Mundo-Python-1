'''Faça um programa que leia um ângulo qualquer e mostre na tela
o valor do seno, cosseno e tangente desse ângulo'''


import math
an = float(input('Qual o algolo desejado para o calculo:'))

seno = math.sin((math.radians(an)))
print(f'O ângulo de {an} tem o seno de {seno:.2f}')

cosseno = math.cos((math.radians(an)))
print(f'O ângulo de {an} tem o cosseno de {cosseno:.2f}')

tang= math.tan(math.radians(an))
print(f'O angolo de {an} tem a tangente de {tang:.2f}')