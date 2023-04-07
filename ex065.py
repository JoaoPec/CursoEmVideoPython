c = ''
maior = 0
menor = 0
i = 0
m = 0
s = 0
while c != 'n':
    n = int(input('Digite um número: '))
    s += n
    if i == 0:
        maior = menor = n
    else:
        if n > maior:
            maior = n 
        if n < menor:
            menor = n
    c = str(input('Quer continuar? [S] [N] ')).lower()
    i += 1
m = s/i
print(f'Você digitou {i} números e a média foi {m}')
print(f'O maior valor digitado foi {maior} e o menor foi {menor}')
