import datetime 
a = int(input('Digite seu ano de nascimento: \n'))
print('===' * 15)
d = int(datetime.date.today().year)

a = d - a

print(f'Você tem {a} anos, você se encaixa na categoria: \n')
if(a <= 9):
    print('MIRIM')
elif(a > 9 and a <= 14):
    print('INFANTIL')
elif(a > 14 and a <= 19):
    print('JUNIOR')
elif (a >19 and a <= 20):
    print('SENIOR')
elif(a > 20 ):
    print('MASTER')
