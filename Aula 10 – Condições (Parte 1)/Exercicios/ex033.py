n1=float(input('Insira o primeiro número: '))
n2=float(input('Insira o segundo número: '))
n3=float(input('Insira o terceiro número: '))
#verificando o maior número
if n1 > n2 and n1 > n3:
    print(f'{n1} é o maior número dentre os três')
if n2 > n1 and n2 > n3:
    print(f'{n2} é o maior número dentre os três')
if n3 > n1 and n3 > n2:
    print(f'{n3} é o maior número dentre os três')

#Verificando o menor número
if n1 < n2 and n1 < n3:
    print(f'{n1} é o menor número dentre os três')
if n2 < n1 and n2 < n3:
    print(f'{n2} é o menor número dentre os três')
if n3 < n1 and n3 < n2:
    print(f'{n3} é o menor número dentre os três')