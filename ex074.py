from random import randint

nu = ()
for c in range (5):
    nuu = (randint(1,100),)
    nu += nuu
print(f'Números gerados: {nu}')
print('O menor número foi: ',min(nu))
print('O maior número gerado foi: ',max(nu))

