v = int(input('Digite o 1° valor: '))
v2 = int(input('Digite o 2° valor: '))
c = ''
while c != 5:
    c = int(input('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa '))
    if c == 1:
        print(v + v2)
    elif c == 2:
        print(v * v2)
    elif c == 3:
        if v > v2:
            print(f'O maior valor é {v}')
        else:
            print(f'O maior valor é {v2}')    
    elif c == 4:
        v = int(input('Digite o 1° valor: '))
        v2 = int(input('Digite o 2° valor: '))
    elif c == 5:
        break
print('Fim do programa.')
