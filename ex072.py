contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
            'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
for c in range(0, len(contagem)):
    n = int(input('Digite um número para receber seu valor por extenso: '))
    if n > 20 or n < 0:
        break
    else:
        print(contagem[n])
