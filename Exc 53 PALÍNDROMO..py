print('-'*11)
print('PALÍNDROMOS')
print('-'*11)
frase = input('Digite uma frase qualquer: ').upper().strip().split()
frasejunta = ''.join(frase)
q = len(frasejunta)
print('O inverso de {} é {}.'.format(frasejunta, frasejunta[::-1]))
inverso = frasejunta[::-1]
tot = 0
for c in range(0, q):
    if frasejunta[c] == inverso[c]:
        tot += 1
    else:
        tot += 0
if tot == q:
    print('Portanto, \033[1;92mé um palíndromo\033[m!')
else:
    print('Portanto, \033[1;91mnão é um palíndromo\033[m.')