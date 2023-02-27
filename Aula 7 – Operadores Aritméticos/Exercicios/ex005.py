"""Faça um programa que leia um número inteiro e mostre na tela seu sicessor e
seu antecessor"""

# +  Soma
# -  Subtração
# *  Multiplicação
# /  Divisão
# ** potência
# // Divisão inteira
# %  Resto da divisão


v = int(input('Me diga um número e eu mostrarei seu antecessor e seu sucessor!:'))
v2 = v - 1
v3 = v + 1
print(f'O antecessor do número {v} é {v2} o Sucessor do mesmo é {v3}')
v4 = v * v
v5 = v / v
v6 = v // v
v7 = v % v
print(f'A multiplicação desse número é {v4} e a divisão dele {v5}.')
print(f'A divisão inteira dele é de {v6} e o resto dessa divisão {v7}')

#Criar a ríz quadrada de um número é a mema coisa que cria a potência de por meio(1/2)
v8 = v ** (1/2)
#Cria a raíz cúbica é o mesmo que criar a potência por um terço(1/3)
v9 = v ** (1/3)
print(f'A raís quadrada de {v} é {v8}')
print(f'O número {v} ao cubo é {v9}')
