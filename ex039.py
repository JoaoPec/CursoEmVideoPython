i = int(input(''))

if(i < 18):
    i = 18 - i
    print(f'ainda vai se alistar.\n Faltam {i} anos')
elif(i == 18):
    print('Hora de se alistar.')
elif(i >18):
    i = i - 18
    print(f'Já passou da hora de se alistar. Você devia ter se alistado a {i} anos')
    