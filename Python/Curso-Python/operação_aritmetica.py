#nome = input('Qual é o seu nome? ')
#print('Prazer em te conhecer {:=^20}!'.format(nome))
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
som = n1 + n2
mul = n1 * n2
sub =  n1 - n2
div = n1 / n2
divint = n1 // n2
exp = n1 ** n2
print(f'A soma vale {som}, o produto é {mul} e a divisão é {div:.2f}', end = ' ') # end=' ' substitui o \n padrão por um espaço, mantendo a próxima saída na mesma linha
print(f'A divisão inteira é {divint} e a potência é {exp}')