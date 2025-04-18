print('-='*8)
print('PA REMASTERIZADA')
print('-='*8)
cont = 1
pt = float(input('Me diga o \033[1;94mprimeiro termo\033[m de sua PA: '))
rz = float(input('Me diga a \033[1;94mrazão\033[m de sua PA: '))
print('Os \033[1;94m10 primeiros termos de sua PA\033[m são:', end='')
print(' \033[4m{}\033[m'.format(pt), end='')
while cont < 10:
    termos = pt + rz
    pt = termos
    if cont <= 8:
        print(', \033[4m{}\033[m'.format(termos), end='')
    elif cont == 9:
        print(' e \033[4m{}\033[m.'.format(termos), end='')
    cont += 1

