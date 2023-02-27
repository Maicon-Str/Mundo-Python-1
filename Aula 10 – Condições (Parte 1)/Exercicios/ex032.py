"""Faça um programa que leia um ano qualquer e mostre se ele é bissexto."""

from datetime import *

ano= int(input('Qual ano deseja analizar? Digite 0 pra ano atual: '))

if ano == 0:
    ano = date.today().year

if ano%2 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'\033[32m{ano} é um ano bissexto. Um ano bissexto tem 366 dias, sendo este dia a mais o 29 de fevereiro.')
else:
    print(f'\033[33m{ano} é um ano  normal de 365 dias.')