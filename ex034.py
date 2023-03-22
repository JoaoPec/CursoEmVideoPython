s = float(input('Digite o seu salário'))

if(s > 1250.00):
    a = s * 0.10
else:
    a = s * 0.15

ts = a + s

print(f"Parabéns! Você recebeu um aumento de {a:.2f}R$...\nSeu novo salário é de {ts:.2f}R$")
