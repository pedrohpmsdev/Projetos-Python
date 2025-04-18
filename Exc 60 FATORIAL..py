print('=='*4)
print('\033[4;91mFATORIAL\033[m')
print('=='*4)
n = int(input('Escolha um número inteiro: '))
print('Calculando {}! = '.format(n), end='')
print('{}'.format(n), end='')
j = n - 1
prod = 0
while j != 0:
    print (' X {}'.format(j), end='')
    prod = n * j
    n = prod
    j -= 1
print(' = \033[4;91m{}\033[m'.format(prod))

#COM O FOR:
'''n = int(input('Digite um número: '))
print('{}'.format(n), end='')
for c in range(n-1, 0, -1):
    print(' X {}'.format(c), end='')
    prod = n * c
    n = prod
print(' = {}.'.format(prod))'''



