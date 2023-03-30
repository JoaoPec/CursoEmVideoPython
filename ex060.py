f = int(input('Digite um número para calcular a sua fatorial: '))
fat = 1
while f != 1:
    fat *= f
    print(f'{f} x', end=' ')
    f -= 1
print(f'1 = {fat}')
