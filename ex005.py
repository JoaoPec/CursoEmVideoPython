#Algorithm that show the antecessors and successor of a determined number.
n = int(input(''))
dn = n + 1 
bn = n - 1  
print('The number {} has {} as it sucessor '.format(n,dn,), end = '')
print('and {} as it antecessor.'.format(bn))