print('-=-'*5)
print('\033[1;96mTONINHO MOTORS\033[m')
print('-=-'*5)
sal = float(input('Qual o seu \033[1;92msalário atual\033[m? '))
if sal > 1250:
    nsal = sal * 1.1
    print('Seu \033[1;92mnovo salário\033[m, com um \033[1;92maumento\033[m de \033[1;92m10%\033[m, é de \033[1;92m{:.2f}\033[mR$.'.format(nsal))
else:
    nsal = sal *1.15
    print('Seu \033[1;92mnovo salário\033[m, com um \033[1;92maumento\033[m de \033[1;92m15%\033[m, é de \033[1;92m{:.2f}\033[mR$.'.format(nsal))