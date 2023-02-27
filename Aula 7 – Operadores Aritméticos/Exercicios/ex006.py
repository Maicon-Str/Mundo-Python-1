#Crie um algoritimo que leia um número e mostre seu dobro, triplo e sua raíz quadrada

v = int(input('Valor a transmutar:'))
v1 = v *2
v2 = v *3
v3 = v **(1/2)
print('Seu número ao quadrado é {}, ao cubo é {}, e sua raiz quasdrada fica como {}'.format(v1, v2, v3))

v = int(input('Valor sem objetos:'))
print(f'O quadrado é {v1}\nO cubo é {v2}\nA raiz quadrada {v3}')
