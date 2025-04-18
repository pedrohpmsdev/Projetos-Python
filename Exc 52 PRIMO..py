print('-'*13)
print('PRIMO OU NÃO?')
print('-'*13)
p = 0
n = int(input('Digite um valor: '))
for c in range (1, n+1):
    if n % c == 0:
        p += 1
        print('\033[1;92m{}\033[m'.format(c), end=' ')
    else:
        print('\033[1;91m{}\033[m'.format(c), end=' ')
if p == 2 and n != 1:
    print('. O número {} é primo!'.format(n))
else:
    print('. O número {} não é primo!'.format(n))