s = ''
m = 0
f = 0
while s != 'exit':
    s = (input('Digite o seu sexo (M) ou (F): (se quiser sair digite exit)')).lower()
    if (s == 'm'):
        print('Sexo masculino digitado com sucesso')
        m += 1
    elif (s == 'f'):
        print('Sexo feminino digitado com sucesso')
        f += 1
    else:
        print('Dado inválido, por favor digite novamente.')
print(f'São {f} mulheres e {m} homens.')