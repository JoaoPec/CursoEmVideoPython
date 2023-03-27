
for c in range(1, 10):
    f = input('Digite uma frase para saber se ela é um palindromo: \n').replace(' ','')
    p = (f[::-1])
    if (f == p):
        print('A frase é um palindromo!')
        break
    else:
        print('A frase não é um palindromo.')
