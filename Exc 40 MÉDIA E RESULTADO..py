print('-'*15)
print('\033[1;94mPORTAL DO ALUNO\033[m')
print('-'*15)
n1 = float(input('Qual foi a sua nota na \033[1;94mPRIMEIRA PROVA\033[m?: '))
n2 = float(input('Qual foi a sua nota na \033[1;94mSEGUNDA PROVA\033[m?: '))
m = (n1+n2)/2
if m >= 7:
    print('\033[1;92mParabéns\033[m! Sua média foi \033[1;92m{}\033[m e você foi \033[1;92maprovado\033[m!'.format(m))
elif 5 <= m <= 6.9:
    print('\033[1;93mFoi por pouco\033[m! Sua média foi de {} e você \033[1;93mnão foi aprovado direto\033[m, mas está na \033[1;93mrecuperação\033[m!'.format(m))
else:
    print('\033[1;91mVocê foi reprovado\033[m. Sua média foi de {} e \033[1;91mvocê está reprovado\033[m nessa matéria.'.format(m))
