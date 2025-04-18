print('-'*14)
print('SOMA DOS PARES')
print('-'*14)
S: int = 0
c: int = 0
i: int = 0
for v in range(1, 7):
    val = int(input('Digite o \033[4m{}o valor\033[m: '.format(v)))
    if val % 2 == 0:
        S += val
        c += 1
    else:
        i += 1
if c > 0:
    print('A \033[1;91msoma dos {} valores pares\033[m entre os digitados é: \033[1;91m{}\033[m'.format(c, S))
else:
    print('Não foram digitados valores pares.')