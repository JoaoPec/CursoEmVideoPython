p = float(input('Digite o preço do produto\n'))

print('===' * 15)

e = int(input('Escolha a opção de pagamento: \n1 - Dinheiro/Cheque 10prcnt de desconto\n2 - Cartão 5prnct de desconto\n3 - 2x no cartão preço normal\n4 - 3x ou mais 20prcnt de juros\n'))


if(e == 1):
    p = p - (p * 0.10)
    print(f'Preço final: {p}')
elif(e == 2):
    p = p - (p * 0.05)
    print(f'Preço final: {p}')
elif(e == 3):
    print(f'{p}')
elif(e == 4):
    p = p + (p * 0.20)
    print(f'Preço final: {p}')
else: 
    print('Opção inválida')
    