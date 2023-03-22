km = int(input(''))

if (km > 80):
    g = km - 80
    print(f'Você está {g}km/h acima da velocidade permitida de 80km/h.')
    m = g * 7
    print(f'A multa aplicada foi de {m}R$')
