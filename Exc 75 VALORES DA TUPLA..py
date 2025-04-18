from itertools import count
print('='*16)
print('VALORES DA TUPLA')
print('='*16)
cont9 = cond = pares = 0

num = (int(input('Digite o primeiro valor: ')), int(input('Digite o segundo valor: ')),
       int(input('Digite o terceiro valor: ')), int(input('Digite o quarto valor: ')))
print(f'O valor 9 foi digitado {num.count(9)} vezes.')
if 3 in num:
    print(f'A posição do primeiro número 3 foi a {num.index(3)+1}o posição.')
else:
    print(f'O 3 não apareceu nenhuma vez.')
print(f'Os \033[1;91mnúmeros pares\033[m digitados foram ',end='')

for c in range(0,4):
    if num[c] % 2 == 0:
        print(f'\033[1;91m{num[c]}\033[m; ',end='')

''' OU DE UM JEITO MAIS RÚSTICO QUE EU FIZ ANTES DE VER A RESPOSTA:
for c in range(0,4):
    if num[c] == 9:
        cont9 += 1
    if num[c] == 3 and cond == 0:
        posi = c
        cond = 1
print(f'Foram digitados \033[1;93m{cont9} números 9\033[m;')
if cond == 1:
    print(f'O \033[1;92mprimeiro 3\033[m aparece na posição \033[1;92m{posi+1}\033[m;')
else:
    print('O \033[1;91mnúmero 3 não apareceu nenhuma vez\033[m;')
c = 0'''