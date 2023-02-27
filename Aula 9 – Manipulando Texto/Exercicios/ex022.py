#Crie um programa que leie o nome completo de uma pessoa e mostre:


Nome=input('Insira seu nome completo')

#O nome com todas as letras maiúsculas
mai= Nome.upper()
print(f'Seu nome em maiúsculo é{mai}')

#O nome com todas as letras minúsculas
min= Nome.lower()
print(f'Seu nome em minúsculo é{min}')

#Quantas letras ao todo(Sem considerar os espaços)

no= len(Nome)
no2= len(Nome.replace(" ","").strip())

print(f'Tamanho do seu nome com os espaço tem {no} e sem os espaços tem {no2}')

#Quantas letras tem o primeiro nome

div= len(Nome.split()[0])
print(f'O Seu primeiro nome tem {div} caracteres')