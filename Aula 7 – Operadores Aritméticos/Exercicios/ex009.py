#Faça um programa que leia um número inteiro qualquer e monstre a sua taboada.

n = int(input('Escolha o número para ver sua taboada:'))

t1 = n * 1
t2 = n * 2
t3 = n * 3
t4 = n * 4
t5 = n * 5
t6 = n * 6
t7 = n * 7
t8 = n * 8
t9 = n * 9
t0 = n * 10
print('---------------')
print('{} x 1 = {}'.format(n, t1))
print('{} x 2 = {}'.format(n, t2))
print('{} x 3 = {}'.format(n, t3))
print('{} x 4 = {}'.format(n, t4))
print('{} x 5 = {}'.format(n, t5))
print('{} x 6 = {}'.format(n, t6))
print('{} x 7 = {}'.format(n, t7))
print('{} x 8 = {}'.format(n, t8))
print('{} x 9 = {}'.format(n, t9))
print('{} x 10 = {}'.format(n, t0))
print('----------------')
print('-'*15)

int(input('Sua taboada programada mais fácilmente:'))
print('{} x {:2} = {}'.format(n, 1, n*1))
print('{} x {:2} = {}'.format(n, 2, n*2))
print("{} x {:2} = {}".format(n, 3, n*3))
print('{} x {:2} = {}'.format(n, 4, n*4))
print(f'{n} x {5:2} = {n*5}')
print('{} x {:2} = {}'.format(n, 6, n*6))
print('{} x {:2} = {}'.format(n, 7, n*7))
print('{} x {:2} = {}'.format(n, 8, n*8))
print('{} x {:2} = {}'.format(n, 9, n*9))
print(f'{n} x {10:2} = {n*10}')
print('-'*15)

#O ,format agora pode ser simplificado para simplesmente f' sguido das variaveis, como visto em alguns exemplos acima