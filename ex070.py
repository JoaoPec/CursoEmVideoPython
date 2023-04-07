tg = 0
pm = 0 
menor = float('inf')
nome_menor = ''
while True:
    n = input('Digite o nome do produto: ')
    p = float(input('Digite o preço do produto: '))
    
    tg += p
    if p > 1000:
        pm += 1 
        
    if p < menor:
        menor = p 
        nome_menor = n
    
    c = input('Gostaria de encerrar o programa? (S) ou (N)').upper()
    if c == 'N':
        break
print(f'Foram gastos {tg:.2f}R$ no total') 
print(f'{pm} produtos custam mais de mil reais')
print(f'O produto de menor preço é {nome_menor} ({menor:.2f}R$)')
