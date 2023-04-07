tn = 0 
while True:
    v = int(input('Digite quanto quer sacar: '))
    
    n100 = v // 100
    v %= 100
    n50 = v // 50
    v %= 50
    n20 = v // 20
    v %= 20
    n10 = v // 10
    v %= 10
    n5 = v // 5
    v %= 5
    n1 = v
    tn += (n100 + n50 + n20 + n10 + n5 + n1)
    
    print(f'Total de cédular: {tn}\nCédulas sacadas: ', end =' ')
    if n100 > 0:
        print(f'{n100} de R$ 100,', end='')
    if n50 > 0:
        print(f'{n50} de R$ 50,', end=' ')
    if n20 > 0:
        print(f'{n20} de R$ 20,', end=' ')
    if n10 > 0:
        print(f'{n10} de R$ 10,', end=' ')
    if n5 > 0:
        print(f'{n5} de R$ 5,', end=' ')
    if n1 > 0:
        print(f'{n1} de R$ 1.', end='\n')
        
    tn = 0