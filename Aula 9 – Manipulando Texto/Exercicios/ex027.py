"""Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
o primeiro e o último nome separadamente """

nome= str(input('Nome completo:')).strip().upper().split()

print(f'O primeiro nome é: {nome[0]}')
print(f'O segundo nome é: {nome[1]}')
print(f'O penúltimo nome é: {nome[len(nome)-3]}')
print(f'O último nome é: {nome[len(nome)-1]}')
