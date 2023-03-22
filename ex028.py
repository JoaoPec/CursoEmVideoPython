import random

c = random.randint(1, 5)

p = int(input('Chute o número que o computador pensou (1 a 5): '))
if (p > 5 or p < 0 ):
    print('Número inválido! Chute um valor de 1 a 5.')
elif(p == c):
    print(f'Parabéns! Você acertou. O número pensado pelo computador foi {c}')
else:
    print(f'Errouuuuu, O número pensado pelo computador foi {c}')
