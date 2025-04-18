from random import choice
from time import sleep

print('='*9)
print('\033[4mJO KEN PÔ\033[m')
print('='*9)
l = ['PEDRA', 'PAPEL', 'TESOURA']
r = choice(l)
es = input('Vamos jogar!(escolha pedra, papel ou tesoura): ').upper()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
if r == es:
    print('Nós escolhemos o mesmo, \033[4m{}\033[m. Deu empate!'.format(es))
elif r == 'TESOURA' and es == 'PEDRA':
    print('COMPUTADOR: \033[4m{}\033[m -- VOCÊ: \033[4m{}\033[m.'.format(r, es))
    print('Você venceu!!!')
elif r == 'PEDRA' and es == 'TESOURA':
    print('COMPUTADOR: \033[4m{}\033[m -- VOCÊ: \033[4m{}\033[m.'.format(r, es))
    print('Eu venci!!!')
elif r == 'TESOURA' and es == 'PAPEL':
    print('COMPUTADOR: \033[4m{}\033[m -- VOCÊ: \033[4m{}\033[m.'.format(r, es))
    print('Eu venci!!!')
elif r == 'PAPEL' and es == 'TESOURA':
    print('COMPUTADOR: \033[4m{}\033[m -- VOCÊ: \033[4m{}\033[m.'.format(r, es))
    print('Você venceu!!!')
elif r == 'PEDRA' and es == 'PAPEL':
    print('COMPUTADOR: \033[4m{}\033[m -- VOCÊ: \033[4m{}\033[m.'.format(r, es))
    print('Você venceu!!!')
elif r == 'PAPEL' and es == 'PEDRA':
    print('COMPUTADOR: \033[4m{}\033[m -- VOCÊ: \033[4m{}\033[m.'.format(r, es))
    print('Eu venci!!!')