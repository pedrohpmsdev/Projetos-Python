from datetime import date
print('!'*12)
print('ANO BISSEXTO')
print('!'*12)
ano = int(input('Digite um \033[4;37mano\033[m qualquer: (Para \033[1;95mano atual\033[m, digite \033[4;37m"0"\033[m)'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0:
    print('O \033[4;37mano\033[m de \033[4;37m{}\033[m é \033[4;95mbissexto\033[m!'.format(ano))
elif ano % 100 == 0 and ano % 400 == 0:
    print('O \033[4;37mano\033[m de \033[4;37m{}\033[m é \033[4;95mbissexto\033[m!'.format(ano))
else:
    print('O \033[4;37mano\033[m de \033[4;37m{}\033[m \033[4;91mnão\033[m é \033[4;95mbissexto\033[m!'.format(ano))