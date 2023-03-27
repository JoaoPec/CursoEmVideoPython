m = 0
mp = 0

for c in range(1,6):
    p = int(input(f'Digite o peso da {c}º pessoa: '))

    if (c == 1):
        mp = p
        m = p 
    if (p > mp):
        mp = p
    if (p < m):
        m = p
    
print(f'O maior peso digitado foi: {mp}kg')
print(f'O menor peso digitado foi: {m}kg')
