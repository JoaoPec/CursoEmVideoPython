#Show the price of a product when inmplemented a 5% discount   

p = float(input('Digite o valor do próduto para que ele receba 5%" de desconto.'))

d = (p * 0.05)
dd = p - d 

print(f'O valor descontado de {p} é {dd:.2f}.'.format(dd))
