import math

n = int(input())

m = n // 1000
n %= 1000

c = n // 100
n %= 100

d = n // 10
n %= 10

u = n // 1
n %= 1

print(f'Unidade: {u:}')
print(f'Dezena: {d:}')
print(f'Centena: {c:}')
print(f'Milhar: {m:}')

