#Desenvolva um programa que leia a notas de um aluno, calcule e mostre sua média.

n1 = float(input('Nota 1:'))
n2 = float(input('Nota 2:'))
n3 = float(input('Nota 3:'))
n4 = float(input('Nota 4:'))
n5 = float(input('Nota 5:'))
n6 = float(input('Nota 6:'))
mt = (n1 + n2 + n3 + n4 + n5 + n6)/6
print('A Média das suas notas,{:.1f},{:.1f},{:.1f},{:.1f},{:.1f},{:.1f} na prova de matemática é:{:.1f}'.format(n1, n2, n3, n4, n5, n6, mt))

#dica 1= Caso queria apenas um número após o ponto usa (:.1f) caso queira mais de 1 substitua
# o número antes do f
