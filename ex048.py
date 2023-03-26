m = 0 

for c in range(0, 500):
    if (c % 3 == 0):
        print(c)
        m += c
        
print(f'A soma é: {m}')