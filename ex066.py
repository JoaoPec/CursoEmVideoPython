s = 0
i = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n != 999:
        s += n 
        i += 1
    else: 
        break 
print(f'Foram digitado {i} números, a soma entre eles é {s}')
