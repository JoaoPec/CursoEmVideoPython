from time import sleep

import emoji

n = 10

print('Falta pouco para o ano novo!')
sleep(1)

for c in range(10, 0, -1):
    print(f'{n}!')
    sleep(1)
    n -= 1

print(emoji.emojize('Feliz ano novo!:fireworks:'))
