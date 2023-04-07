import random

while True:
    n = int(input('Digite um valor '))
    uc = input('[P]/[I] ').upper
    pc = random.randint(1,10)
    if pc % 2 == 0:
       pp = 'P'
    else:
        pp = 'I'
    s = n + pc     
    if s % 2 ==0:
        r = 'P'
    else:
        r = 'I'
    if uc == r:
        print('Parabéns você venceu!')
        break
    else:
        print('Você perdeu.')
        