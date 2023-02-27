#Crie um programa de leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.

real = float(input('Quanto você tem de dinheiro em reais: R$'))
dolar = real / 5.70
iene = real /  0.052
euro = real /  6.82
print('Com seus {} você é capaz de comprar:{:.2f} Dólares, {:.2f} ienes japonêses ou {:.2f} Euros'.format(real, dolar, iene, euro))