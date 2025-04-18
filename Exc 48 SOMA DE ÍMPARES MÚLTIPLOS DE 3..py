print('='*44)
print('SOMA DE ÍMPARES MÚLTIPLOS DE 3 ENTRE 1 E 500')
print('='*44)
S: int = 0
g: int = 0
for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        S += c
        g+= 1
print('A \033[1;91msoma\033[m de todos os \033[1;92m{} ímpares múltiplos de 3 entre 1 e 500\033[m é: \033[1;91m{}\033[m'.format(g, S))