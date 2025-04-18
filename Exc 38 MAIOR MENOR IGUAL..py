print('\033[1;93mMAIOR\033[m, \033[1;93mMENOR\033[m OU \033[1;94mIGUAL\033[m?')
n1 = float(input('Digite o \033[1;91mprimeiro valor\033[m: '))
n2 = float(input('Digite o \033[1;91msegundo valor\033[m: '))
if n2 > n1:
    print('\033[1;93mMAIOR\033[m: \033[1;93m{}\033[m.'.format(n2))
    print('\033[1;93mMENOR\033[m: \033[1;93m{}\033[m.'.format(n1))
elif n1 > n2:
    print('\033[1;93mMAIOR\033[m: \033[1;93m{}\033[m.'.format(n1))
    print('\033[1;93mMENOR\033[m: \033[1;93m{}\033[m.'.format(n2))
else:
    print('Os valores digitados são \033[1;94miguais\033[m.')