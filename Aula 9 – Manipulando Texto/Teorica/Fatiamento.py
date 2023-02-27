frase= "Curso em Video Python"
# Seleciona o caractere relacionado ao número.
print(frase[9])

#Seleciona o caractere até o décimo segundo
print(frase[9:13])

#seleciona caracteres pulano de dois em dois
print(frase[9:21:2])

#Do ínicio até o quarto caractere
print(frase[:5])

#Do Caractere 15 até o final
print(frase[15:])

#Seleciona do 9 ao final, pulando de três em três
print(frase[9::3])

#Len analisa o cumprimento da string(linha de texto)
print(len(frase))

#Conta um número específico de letras com critérios especificos.(Numero de letras O na string)
print(frase.count('o'))
#Número de letras O do zero ao treze(nota-se que a seleção para no 13 e não o seleciona)
print(frase.count('o',0,13))

#Função"Find" Me diz quantas vezes encontrou uma selação epecífica
print(frase.find('deo'))

#Existe tal selação na string? Será respondido com true
print('Curso' in frase)

#Funcção "Transformação". Muda, adiciona substitui 
print(frase.replace('Python','Android'))

#Método "Upper" Transforma letras em maiúsculas
print(frase.upper())

#Metodo "lower" Transforma letras em minúsculas
print(frase.lower())

#Metodo "Capitalize" transforma o primeiro caractere da string para maiúsculo
print(frase.capitalize())

#Metodo title, transforma o primeiro caractere de palavra por palava em maiúscula
print(frase.title())

#Metodo "Strip" Remove os espaços inúteis de uma string
frase2='     Aprenda Python  '
print(frase2)
print(frase2.strip())
#Se colocardo 'r' antes do strip, é tratada a direita primeiro se usado 'l' é tratado a esquerda

#Conta o número de caracteres em uma frase inteira(incluindo os espaços)
print(len.frase2)
#DIVISÃO

#Função "split" divide uma string em várias palavras, colocando cada uma em sua própria lista.
print(frase2.split())

#Função "join" junta uma coisa na outra. Nota-se que '' podem ser preenchidos com que vc quiser.
print(' '.join(frase2))