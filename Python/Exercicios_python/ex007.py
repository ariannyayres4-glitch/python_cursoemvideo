n1 = float(int(input('Lagrgura da parede: ')))
n2 = float(input('Altura da parede: '))
area = n1*n2
tinta = (area / 2 )
print(f'Sua parede tem a dimensão de {n1}X{n2} e sua área é de {area}m²')
print(f'Para pintar essa parede, você precisará de {tinta}l de tintas')