n = int(input('Digite um número para verificar se ele é primo: '))

if (n == 1):
    print(f'{n} não é primo')
for c in range(2, n):
    if n % c == 0:
        print(f'O número {n} não é primo.')
        break
else:
    print(f'O número {n} é primo!')

3