"""Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo."""

from time import sleep

print('\033[35mVALORES ESCOLHIDOS\n')

comprimento_1= float(input('\033[37mValor 1: '))
comprimento_2= float(input('Valor 2: '))
comprimento_3= float(input('Valor 3: '))

print('-=-' * 20)

print('\033[35mANALISE DOS VALORES\n')
#Encontrar a Maior
maior_comprimento= comprimento_1

if comprimento_2 > comprimento_1 and comprimento_2 > comprimento_3:
    maior_comprimento= comprimento_2
if comprimento_3 > comprimento_1 and comprimento_3 > comprimento_2:
    maior_comprimento= comprimento_3

print(f'\033[37mA maior reta: {maior_comprimento}')

#ENCONTRAR O MENOR
menor_comprimento= comprimento_1

if comprimento_2 < comprimento_1 and comprimento_2 < comprimento_3:
    menor_comprimento= comprimento_2
if comprimento_3 < comprimento_1 and comprimento_3 < comprimento_2:
    menor_comprimento= comprimento_3

print(f'A menor reta: {menor_comprimento}')

#ENCONTRAR O MEDIANO
if comprimento_1 < comprimento_2 and comprimento_1 > comprimento_3 or comprimento_1 > comprimento_2 and comprimento_1 < comprimento_3:
    medio_comprimeito= comprimento_1
if comprimento_2 < comprimento_1 and comprimento_2 > comprimento_3 or comprimento_2 > comprimento_1 and comprimento_2 < comprimento_3:
    medio_comprimeito= comprimento_2
if comprimento_3 < comprimento_2 and comprimento_3 > comprimento_1 or comprimento_3 > comprimento_2 and comprimento_3 < comprimento_1:
    medio_comprimeito= comprimento_3

print(f'A intermediária: {medio_comprimeito}')
print('-=-' *20)
print('ANALISANDO...')
sleep(2)

#Resultado 
print('\033[33mSuas retas formarão um triângulo se os menores entre elas alcançarem, ou, ultrapassarem a maior: \n')
if menor_comprimento < medio_comprimeito + maior_comprimento and medio_comprimeito < menor_comprimento + maior_comprimento and maior_comprimento < menor_comprimento + medio_comprimeito:
    print('\033[32mSim! Com essas retas pode existir um triângulo!')
else:
    print('\033[31mNão! Com essas retas é impossível existir um triângulo!')