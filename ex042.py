a = float(input(''))
b = float(input(''))
c = float(input(''))

if (c > (a - b) and (c < (a + b))) and (a > (b - c) and (a < (b + c))) and ((b > (a - c)) and (b < (a + c))):
    print('FORMA UM TRIANGULO')
    print('===' * 15)
else:
    print('Não forma um triangulo!')
    exit()
if a == b == c:
    print('triângulo equilátero.')
    exit()
if (a == b or b == c or c == a):
    print('triângulo isóceles')
elif (a != b and b != c and c != a):
    print('triangulo escaleno')
