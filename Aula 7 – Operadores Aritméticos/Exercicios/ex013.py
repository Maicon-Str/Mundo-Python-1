#Faça um algoritimo que leia o salário de um funcionário
#E mostre seu novo salária com 15% de desconto

#sal = float(input('Qual é o seu salário?:R$'))
#p1 = sal * 15 / 100
#p2 = sal + p1
#print('Seu aumento foi de R${:.2f} que no total fica R${:.2f}. Parabéns!'.format(p1, p2))

Au  = float(input('Você está prestes a receber um aumento. Qual a porcentagem?'))
Sal = float(input('Poderia me dizer qual o seu salário atual?'))
p1 = Sal*Au/100
p2 = Sal + p1
print(f'Seu aumento salarial foi de {p1:.2f} e o total do seu novo salário atual é de {p2:.2f}')