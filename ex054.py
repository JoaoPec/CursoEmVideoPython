import datetime
mi = 0
Mi = 0
for c in range(0,7):
    a = int(input('Digite o seu ano de nascimento:'))
    an = datetime.date.today().year
    i = an - a 
    if(i >= 18):
        Mi += 1
    elif(i <18):
        mi += 1 
print(f'Existem {Mi} passoas maior de idade.\ne')
print(f'{mi} Pessoas menor de idade.')
