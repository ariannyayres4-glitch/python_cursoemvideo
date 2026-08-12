n1 = float(input('Qual o preço do produto? R&'))
desb = float(input('Qual o valor do desconto?(não use o sinal de %) '))
des = n1*(desb/100)
preco = n1-des
print(f'O produto que custava R${n1:.2f}, na promoção com desconto de {desb:.0f}% vai custar R${preco:.2f}.')