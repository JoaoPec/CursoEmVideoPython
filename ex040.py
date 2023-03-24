n = float(input('Digite nota 1: '))
n2 = float(input('Digite nota 2: '))

m = (n + n2) / 2
print('\n')

print(f'A média foi: {m} \n')
if (m < 5):
    print('REPROVADO')
elif (m >= 5 and m <= 6.9):
    print('RECUPERAÇÃO')
elif (m >= 7):
    print('APROVADO')
