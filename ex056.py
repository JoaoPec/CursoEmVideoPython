nh = '' 
hv = 0
mv = 0
ti = 0

for c in range(0,4):
    n = input(str('Digite o seu nome: '))
    i = int(input('Digite a sua idade: '))
    s = input(str('Digite seu sexo (F) ou (M): ')).upper()
    
    if (s == 'M' and i > hv):
        hv = i
        nh = n
    if (s == 'F' and i < 20):
        mv += 1 
    ti += i

m = ti / 4


print(f'O homem mais velho é {nh}')
print(f'Existem {mv} mulheres com menos de 20 anos')
print(f'A média de idade de todos é: {m}')
