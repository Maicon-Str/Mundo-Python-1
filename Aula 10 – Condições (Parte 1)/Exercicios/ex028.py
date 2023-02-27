"""Escreva um programa que faça o computador “pensar” em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu."""

import random
# from random import radint(Para carregar um punico método e otmizar o programa )
from time import sleep
import colorsys
print('-=-' *20)
print('''As máquinas enlouqueceram e quererm dominar o mundo
Só você pode impedir essa catastrofe vencendo a I.A Mãe em um jogo
Está preparado?''')
print('-=-' *20)
eu= int(input('Digite o número que a I.A está pensando e salve a todos nós! :'))
print('PROCESSANDO...')
sleep(2)
resultado= random.randint(0, 5)
# resultado = radint(0, 5) (Se otmizado com um único método)

if eu == resultado:
    print('\033[32mMeu Deus, Você conseguiu! Salvou a todos nós, Viva!!!') #\033 é o código de cores Ansi
else:
    print(f'\033[1;31mAh não, você errou... Ela pensou no {resultado}. Estamos condenados, todos condenados.')
