#Faça um programa que leia a largura e a altura de uma parede em metros.
#Calcule a sua área e a quantidade de tinta necessária para pinta-la.
#Sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

l = float(input('Largura da Parede:'))
a = float(input('Altura da parede:'))
m2 = l * a
print(f'sua parede tem tem a dimensão de {l}x{a} e mede {m2} metros quadrados.')
tin =m2/ 2
print(f'E para pintar uma parede nessas dimensões é necessário {tin} litros de tinta!')