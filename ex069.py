p18 = 0
m20 = 0
nh = 0

while True:
    i = int(input('Digite a sua idade:'))
    s = input('Qual o seu sexo? (H) ou (F) ').upper()
    if i > 18:
        p18 += 1
    if i < 20 and s == 'F':
        m20 += 1
    if s == 'H':
        nh += 1
    c = input('Você quer continuar? (S) ou (N)').upper()
    if c == 'N':
        break
    
print(f'{p18} pessoas tem mais de 18 anos')
print(f'{nh} homens foram cadastrados')
print(f'{m20} mulheres tem menos de 20 anos')
    