diab = float(input('Quantos dias foram alugados? '))
kmb = float(input('Quando km foram rodados? '))
total = (diab * 60) + (kmb * 0.15)
print(f'O total a pagar é de R&{total:.2f}')
