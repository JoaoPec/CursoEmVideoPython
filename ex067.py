import random

vitorias_consecutivas = 0

while True:
    numero_jogador = int(input('Digite um número entre 0 e 10: '))
    escolha_jogador = input('Par ou ímpar? [P/I] ').strip().upper()
    numero_pc = random.randint(0, 10)
    soma = numero_jogador + numero_pc
    resultado = 'P' if soma % 2 == 0 else 'I'
    print(f'Você jogou {numero_jogador} e o computador jogou {numero_pc}.')
    print(f'A soma deu {soma} e o resultado foi {resultado}.')
    if resultado == escolha_jogador:
        print('Você venceu!')
        vitorias_consecutivas += 1
    else:
        print('Você perdeu!')
        break

print(f'Você conseguiu {vitorias_consecutivas} vitórias consecutivas.')
