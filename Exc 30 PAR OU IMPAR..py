print('-'*13)
print('\033[4mPAR OU ÍMPAR\033[m')
print('-'*13)
n = float(input('Digite um valor e lhe direi se ele é \033[4;91mPAR\033[m ou \033[4;92mÍMPAR\033[m: '))
if n % 2 == 0 and n != 0:
    print('{} é um valor \033[4;91mPAR\033[m.'.format(n))
else:
    print('{} é um valor \033[4;92mÍMPAR\033[m.'.format(n))