from datetime import date
print('-'*10)
print('\033[4mMAIORIDADE\033[m')
print('-'*10)
maioridade = 0
menoridade = 0
for c in range (0, 7):
    nasc = int(input('Em qual ano a {}ª pessoa nasceu? '.format(c+1)))
    idade = date.today().year - nasc
    if idade >= 18:
        maioridade += 1
    else:
        menoridade += 1
print('O número de pessoas na \033[4mMAIORIDADE\033[m é de \033[4m{}\033[m.'.format(maioridade))
print('O número de pessoas na \033[4mMENORIDADE\033[m é de \033[4m{}\033[m.'.format(menoridade))