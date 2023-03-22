n1, n2, n3 = map(int, input('Digite três valores separados por espaço para serem ordenados: ').split())

if (n1 > n2):
    a = n1
    n1 = n2
    n2 = a
if (n2 > n3):
    a = n2
    n2 = n3
    n3 = a
if (n3 < n1):
    a = n3
    n3 = n1
    n1 = a12
if (n1 > n3):
    a = n1
    n1 = n3
    n3 = a

print(f'{n1} {n2} {n3}')
