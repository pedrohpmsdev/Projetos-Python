print('-='*8)
print('PA REMASTERIZADA')
print('-='*8)
cont = 1
qnt = 10
total = 0
pt = int(input('Me diga o \033[1;94mprimeiro termo\033[m de sua PA: '))
rz = int(input('Me diga a \033[1;94mrazão\033[m de sua PA: '))
print('Os \033[1;94m10 primeiros termos de sua PA\033[m são:', end='')
print(' \033[4m{}\033[m'.format(pt), end='')
while qnt != 0:
    total += qnt
    while cont < total:
        termos = pt + rz
        pt = termos
        if cont <= total-2:
            print(' -> \033[4m{}\033[m'.format(termos), end='')
        elif cont == total-1:
            print(' -> \033[4m{}\033[m.'.format(termos))
        cont += 1
    qnt = int(input('Quer ver quantos termos a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
print('|-----------|||-----------|')
print('FINALIZANDO O PROGRAMA...')
print('PROGRAMA FINALIZADO.')

'''print('-='*8)
print('PA REMASTERIZADA')
print('-='*8)
cont = 1
qnt = 1
pt = int(input('Me diga o \033[1;94mprimeiro termo\033[m de sua PA: '))
rz = int(input('Me diga a \033[1;94mrazão\033[m de sua PA: '))
print('Os \033[1;94m10 primeiros termos de sua PA\033[m são:', end='')
print(' \033[4m{}\033[m'.format(pt), end='')
while cont < 10:
    termos = pt + rz
    pt = termos
    if cont <= 8:
        print(', \033[4m{}\033[m'.format(termos), end='')
    elif cont == 9:
        print(' e \033[4m{}\033[m.'.format(termos))
    cont += 1
while qnt != 0:
    qnt = int(input('Quer ver mais quantos termos [0 para nenhum; X para X termos mais]? '))
    if qnt > 0:
        for c in range(1, qnt+1):
            termos = pt + rz
            pt = termos
            if c < qnt:
                print(' -> ', end='')
                print('\033[4m{}\033[m'.format(termos), end='')
            if c == qnt:
                print(' -> \033[4m{}\033[m.'.format(termos))
    elif qnt == 0:
        print('FINALIZANDO O PROGRAMA...')
print('PROGRAMA FINALIZADO.')'''

