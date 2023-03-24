n = int(input('Digite o primeiro valor\n'))
n2 = int(input('Digite o segundo valor\n'))   


if(n > n2):
    print(f'O primeiro valor ({n}) é maior')
elif(n2 > n):
    print(f'O segundo valor ({n2}) é maior')   
elif(n == n2):
    print('Ambos os valores são iguais')
    