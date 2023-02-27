"""Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas."""

from time import sleep

quilometros = float(input('Qual a distância da sua viagem?: ')) #3.535.1 km

print('\033[32mCalculando rota...')
print('\033[33mCalculando preço...')
sleep(3)
if quilometros <= 200: 
    preço_passagem_curta= quilometros * 0.50
    print(f'Sua passagem de {quilometros} custará R${preço_passagem_curta:.2f}')
else:
    preço_passagem_longa= quilometros * 0.45
    print(f'Sua viagem de {quilometros} lhe custará R${preço_passagem_longa:.2f}')