"""Crie um programa que leie o nome de uma cidade e se ela começa ou não com a palavra Santo"""


cidade = str(input("Insira o nome da sua cidade")).strip().upper().split()	

#Detecta se começa com a variável escolhida

print(cidade[0] == 'SANTO')