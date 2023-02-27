"""Crie um programa que leia um número inteiro
E diga na tela se ele é PAR ou ÍMPAR"""

from time import sleep

numero = int(input('Digite um número para analizarmos: '))
conta= numero%2
if numero%2 == 0:
    print('ANALIZANDO...')
    sleep(2)
    print('\033[34mSeu número é par!')
else:
    print('ANALIZANDO...')
    sleep(2)
    print('\033[35mSeu número é impar')