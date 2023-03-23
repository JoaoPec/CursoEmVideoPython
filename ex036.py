v = float(input('Qual o valor da casa? \n'))
s = float(input('Qual o seu salário? \n'))
a = int(input('Em quantos anos pretende pagar? \n'))

pm =  v / (a * 12) 

if(pm > (s * 0.30)):
    print(f'\033[31m Emprestimo negado!\033[m \n A prestação mensal excede 30% do seu salário.')
else:
    print(f'\033[32m Emprestimo aprovado! \033[m \n O a prestação mensal será de R${pm:.2f} para ser pago em {a} anos!')
    
