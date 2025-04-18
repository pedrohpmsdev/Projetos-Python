from datetime import date
print('-'*19)
print('\033[1;92mALISTAMENTO MILITAR\033[m')
print('-'*19)
nasc = int(input('Em que \033[4;37mano\033[m você nasceu? '))
idade = date.today().year - nasc
f = abs(18-idade)
if idade < 17:
    print('\033[1;92mFique despreocupado!\033[m \033[1;92mVocê ainda não atingiu a idade de se alistar. Faltam {} anos para o alistamento.\033[m'.format(f))
elif idade == 17:
    print('\033[1;93mFique ligado!\033[m \033[1;93mVocê ainda não atingiu a idade de alistamento, mas ano que vem já é hora de se alistar!\033[m')
elif idade == 18:
    print('\033[1;96mVocê atingiu a idade de se alistar. Faça o alistamento!\033[m')
else:
    print('\033[1;91mA idade de se alistar já passou! É melhor você fazê-lo logo, senão poderá ter problemas com o governo (não recomendo que tenha). Você devia ter se alistado há {} anos.\033[m'.format(f))
