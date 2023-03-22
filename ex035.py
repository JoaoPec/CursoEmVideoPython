a = float(input(''))
b = float(input(''))
c = float(input(''))

if (c > (a - b) and (c < (a + b))) and (a > (b - c) and (a < (b + c))) and ((b > (a - c)) and (b < (a + c))):
    print('Forma um triangulo!')
else:
    print('Não forma um triangulo!')
