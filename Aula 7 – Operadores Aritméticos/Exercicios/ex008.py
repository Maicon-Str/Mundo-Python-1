#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros

km = float(input('Distância em quilômetros desejada a converter:'))

cm = km * 100000
mt = km * 1000
mm = km * (1e+6)
mi = km / 1609
ja = km * 1094
pe = km * 3281
po = km * 39370
mn = km / 1852

print('O valor em {} km equivale a: {} centímetros, {} Metros, {} Milímetros e {} Milhas!'.format(km, cm, mt, mm, mi))
print('O valor em {} km equivale a: {} Jardas, {} Pés, {} Polegadas e {} Milhas Nauticas!'.format(km, ja, pe, po, mn))


metro = float(input(' Medida em metros desejadas:'))
km = metro / 1000
hm = metro / 100
dam = metro / 10
m = metro
dm = metro * 10
cm = metro * 100
mm = metro * 1000
print('O valor em {} Metros corresponde a: {}Quilômetros, {} Hectômetros, {} Decâmetro, {} Metros, {} Decímetro, {} Centímetro, {} Milímetro'.format(metro, km, hm, dam, m, dm, cm, mm))
