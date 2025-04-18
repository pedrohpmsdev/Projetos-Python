print('-'*17)
print('\033[4;93mALUGUEL DE CARROS\033[m')
print('-'*17)
km = float(input('Quantos \033[1;37mKm\033[m foram \033[1;37mrodados\033[m? '))
dia = int(input('Por quantos \033[4mdias\033[m o \033[1;93mcarro\033[m foi \033[1;93malugado\033[m? '))
v1 = dia*60
v2 = km*0.15
print('O \033[1;91mpreço\033[m a \033[1;91mpagar\033[m por \033[4m{} dias\033[m e \033[1;37m{}Km rodados\033[m é de \033[1;91m{}\033[m.'.format(dia, km, v1 + v2))