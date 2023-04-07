n1 = int(input('Digite um valor: '))
n2 = int(input('Mais um: '))
n3 = int(input('Outro: '))
n4 = int(input('O último: '))

t = (n1, n2, n3, n4)
par = 0
numero_de_noves = 0
primeira_posicao_numero_3 = -1

for i in range(len(t)):
    if t[i] == 9:
        numero_de_noves += 1
    if t[i] == 3 and primeira_posicao_numero_3 == -1:
        primeira_posicao_numero_3 = i
    if t[i] % 2 == 0:
        par += 1

print(f'Os valores digitados foram: {t}\n')
print(f'O número nove foi digitado {numero_de_noves} vezes.')
if primeira_posicao_numero_3 != -1:
    print(f'O número três foi primeiramente digitado na posição {primeira_posicao_numero_3}.')
else:
    print('O número três não foi digitado.')
print(f'Foram digitados {par} números pares.')
