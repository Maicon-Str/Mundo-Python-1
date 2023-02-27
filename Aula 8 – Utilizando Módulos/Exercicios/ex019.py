import random

print('Os participantes do sorteio são?')
a = input("Digite um nome:")
b = input('Digite um nome:')
c = input('Digite um nome:')
d = input('digite um nome:')
e = input('digite um nome:')
l = [a, b, c, d, e]
r = random.choice(l)
print(f"O ganhador do sorteio é: {r}")
