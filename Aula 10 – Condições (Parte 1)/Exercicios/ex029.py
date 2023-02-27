"""Escreva um programa que leia a velocidade de um carro.
   Se ele ultrapassar 80km/h, mostre uma mensage
dizendo que ele foi multado.
   A multa deverá custar R$7.00 por cada KM acima do limite."""

from time import sleep

velocidade = float(input('Informe a velocidade do veículo no momento da captura: '))
multa = (velocidade * 7)-560 #560 é o valor deduzido dos 80km já que não há multa sobre ele, sobrando apenas o valor da multa
limite = multa // 7
if velocidade > 80.00:
    print('ANALIZANDO')
    sleep(2)
    print('\033[1;31mInfelizmente você estava acima do limite de velocidade permitida')
    print(f'Você deverá pagar uma multa de R${multa:.2f}, pelos {limite:.0f}km/h acima do limite. Sua conta será imprimida a seguir:')
    print('IMPRIMINDO CONTA...')
    sleep(4)
    print('Tudo pronto, tenha um bom dia!')

else:
    print('ANALIZANDO')
    sleep(5)
    print('\033[1;32mOlá, motorista, está tudo correto, tenha uma boa viagem.')



    #80 * 7,0 = 560