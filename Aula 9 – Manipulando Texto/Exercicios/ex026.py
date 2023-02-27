"""Faça um programa que leia uma frase pelo teclado e mostre:

Quantas vezes aparece a letra A

Em que posição ela aparece a primeira vez

Em que posicão ela aparece a última vez"""
 
frase = str(input(("Insira a frase:")).upper().strip().replace(" ", ""))
letra = str(input('Letra a ser analizada:')).upper().strip()
numero= str(frase.count(letra)).upper()
print(f'A letra {letra} aparece na frase {numero} vezes')

print(f'A primeira letra {letra} aparece na posição: {frase.find(letra)+1}')
print(f'A última letra {letra} aparece na posição: {frase.rfind(letra)+1}')
