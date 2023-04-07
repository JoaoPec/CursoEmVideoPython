t = ('Banana',2.50,'Maçã',4.72,'Barra de chocolate',4.99,'Acem bovino',25.99)

for i in range(0,len(t),2):
    print(f'{t[i]}.............R${t[i + 1]}')
