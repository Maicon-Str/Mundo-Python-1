from random import shuffle
print('Sorteie a ordem de apresentação')
a1 = input('Aluno a:')
a2 = input('Aluno b:')
a3 = input('Aluno c:')
a4 = input('Aluno d:')
lista = [a1, a2, a3, a4]
shuffle(lista)
print(f'A ordem de apresentação sera:{lista}')