"""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
 Para os inferiores ou iguais, o aumento é de 15%."""

salário= float(input('Qual é o seu sálário atual?:  '))

if salário >= 1250.00:
    atual= (salário * 10)/100 + salário
    print(f'Seu salário antido de R${salário:.2f} aumentou para R${atual:.2f}. Parabéns!')
else:
    atual_2= (salário * 15)/100 + salário
    print(f'Seu salário antigo de R${salário:.2f} aumentou para R${atual_2:.2f}. Parabéns!')
