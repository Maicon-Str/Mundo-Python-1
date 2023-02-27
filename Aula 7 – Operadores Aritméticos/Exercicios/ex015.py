a = float(input("Por quantos dias você ficou com o carro?:"))
b = float(input("E quantos quilômetros você percorreu?:"))
dias = 60.00 * a
km = 0.15 * b
total = dias + km
print('O pagamento por dias em posse ficou em {:.2f}R$ e em {:.2f}R$ por quilômetro percorrido'.format(dias, km))
print('Seu total a pagar é de {:.2f}R$'.format(total))
