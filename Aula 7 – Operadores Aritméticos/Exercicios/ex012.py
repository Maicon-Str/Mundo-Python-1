#Faça um algoritimo que leia o preço do produro e mostre seu novo preço com 5% de desconto

#con0 = float(input('Seu desconto é de 5%. Quando vc deseja gastar?:'))
#con1 = float(5*con0)/100
#con2 = con0 - con1
#print(f'Seu desconto toatal foi de R${con1:.2f} e você pagou R${con2:.2f}')

print('-------Calculo de descontos abaixo-------')
Val = float(input("Escolha um valor para ser usado"))
Des = float(input("Agora escolha o desconto desejado"))

Fn = float((Val*Des)/100)
Fn2 = float(Val - Fn)

print(f'Os {Des}% de desconto equivalem a R${Fn:.2f} subtraídos do seu valor de R${Val:.2f}. Logo você pagará R${Fn2:.2f}')
