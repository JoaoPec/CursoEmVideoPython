from random import randint

cp = randint(0,10)

print('Pensei em um número de 1 a 10...\nSerá que você consegue advinha-lo?')
uc = ''
t = 0
while uc != cp:
    t += 1
    uc = int(input(''))
    if uc < cp:
        print('O número que pensei é maior!')
    elif uc > cp:
        print('O número que pensei é menor!')
print(f'Parabéns! você acertou, o número que pensei foi {cp}\nVocê acertou em {t} tentativas!')