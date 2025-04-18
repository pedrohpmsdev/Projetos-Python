print('='*17)
print('\033[1;94mPINTURA DE PAREDE\033[m')
print('='*17)
alt = float(input('Quantos \033[4;96mmetros\033[m de \033[4:96maltura\033[m tem essa parede? '))
comp = float(input('Quantos \033[4;96mmetros\033[m de \033[4;96mcomprimento\033[m tem essa parede? '))
area = alt*comp
L = area/2
print("Sabendo que cada \033[1;94mlitro\033[m de tinta pinta \033[1;91m1/2m^2\033[m, será preciso \033[1;94m{}L\033[m de tinta para pintar a parede de \033[1;91m{}m^2\033[m".format(L, area))