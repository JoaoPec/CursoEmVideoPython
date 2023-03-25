import random

pc = str(input('Escolha entre Pedra Papel e Tesoura: \n').upper())

lista = ["PEDRA", "PAPEL", "TESOURA"]

cc = random.choice(lista)
print(f'O computador escolheu {cc}\n')
if (pc == cc):
    print(f'Empate! ambos escolheram {cc}')
elif (pc == "PEDRA" and cc == "TESOURA"):
    print(f'Pedra vence tesoura. Jogador vence!')
elif (pc == "PAPEL" and cc == "PEDRA"):
    print("Papel vence pedra. Jogador vence!")
elif (pc == "TESOURA" and cc == "PAPEL"):
    print('Tesoura vence papel. Jogador vence!')
elif (cc == "PEDRA" and pc == "TESOURA"):
    print('Pedra vence tesoura. Computador vence!')
elif (cc == "PAPEL" and pc == "PEDRA"):
    print("Papel vence pedra. Computador vence!")
elif (cc == "TESOURA" and pc == "PAPEL"):
    print('Tesoura vence papel. Computador vence!')
else: 
    print('Escolha inválida.')
