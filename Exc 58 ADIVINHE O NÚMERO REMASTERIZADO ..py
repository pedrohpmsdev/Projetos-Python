from random import choice
print('-'*17)
print('ADIVINHE O NÚMERO')
print('-'*17)
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = choice(lista)
n = int(input('Pensei em um número entre \033[4m0 e 10\033[m. Tente adivinhar qual é: '))
tent = 1
if n > 10 or n < 0:
    print('\033[1;91mEsse valor não está dentro dos possíveis\033[m. \033[4mApenas entre 0 e 10\033[m.')
while n != res:
    if n > res:
        n = int(input('\033[1;91mErrado\033[m! Tente novamente (Uma dica: é menor que {}): '.format(n)))
    elif n < res:
        n = int(input('\033[1;91mErrado\033[m! Tente novamente (Uma dica: é maior que {}): '.format(n)))
    tent += 1
    if  n > 10 or n < 0:
        print('\033[1;91mEsse valor não está dentro dos possíveis\033[m. \033[4mApenas entre 0 e 10\033[m.')
print('\033[1;92mParabéns\033[m! Você acertou com {} tentativas. O número que eu pensei foi o \033[4m{}\033[m.'.format(tent, res))

