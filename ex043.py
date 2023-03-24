a = float(input('Digite a sua altura: \n'))
p = int(input('Digite o seu peso: \n'))

imc = p / (a ** 2)
print(f'O seu imc foi de {imc:.1f}\n')

if(imc < 18.5):
    print('Abaixo do peso')
elif(imc >= 18.5 and imc <=25):
    print('Peso ideal')
elif(imc >= 25 and imc <=30):
    print('Sobrepeso')
elif(imc >= 30 and imc <= 40):
    print('Obesidade')
else:
    print('Obesidade mórbida')