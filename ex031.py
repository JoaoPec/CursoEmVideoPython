km = int(input('Digite os km da viagem: '))

if (km <= 200):
    p = km * 0.50
    print(f'O preço da viagem curta ficou {p}R$')
elif (km > 200):
    p = km * 0.45
    print(f'O preço da viagem longa ficou  {p:.2f}R$')
