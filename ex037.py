n = int(input('Digite um valor'))

e = int(input('Você quer transformar esse número em: \n 1 -- binario \n 2 -- octal \n 3 -- hexadecimal \n'))

print ('=' * 15)
print('\n')
if(e == 1):
    n = bin(n)
elif(e == 2):
    n = oct(n)
elif(e == 3):
    n = hex(n)
else:
    print('escolha inválida.')


print(n[2::])
    
