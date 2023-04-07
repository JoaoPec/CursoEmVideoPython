n = 0
c = 0
s = 0 
while n != 999:
    n = int(input('Digite um valor para ser armazenado: (999) para finalizar'))
    if n != 999:
        s += n
        c += 1
print(F'Foram digitados {c} valores, a soma entre eles foi: {s}')
