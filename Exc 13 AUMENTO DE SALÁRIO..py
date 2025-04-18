print('='*8)
print('\033[1;92mPROMOÇÃO\033[m')
print('='*8)
print('Olá, \033[1;94mfuncionário\033[m! Vimos que você está fazendo um \033[1;93mótimo trabalho\033[m e queremos te \033[4;92mpromover\033[m!')
sal = float(input('Qual o seu salário atual? '))
novsal = sal*1.15
print('Seu \033[1;96msalário\033[m de \033[1;96m{}R$\033[m sofreu um \033[1;92maumento\033[m de \033[1;92m15%\033[m, ficando num valor de \033[4;92m{}\033[mR$. Parabéns e continue assim!'.format(sal, novsal))