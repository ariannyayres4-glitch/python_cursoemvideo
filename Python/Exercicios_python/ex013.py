from math import hypot
cto = float(input('Comprimento do cateto oposto: '))
cta = float(input('Comprimento do catetos adjacente: '))
h = hypot(cto, cta)
print(f'A hipotenusa vai medir {h:.2f}')
