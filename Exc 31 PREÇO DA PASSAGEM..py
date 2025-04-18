print('-'*17)
print('\033[1;92mPREÇO DA PASSAGEM\033[m')
print('-'*17)
km = float(input('Quantos \033[1;37mquilômetros\033[m para a viagem? '))
if km <= 200:
    preço = km * 0.5
    print('Sua \033[1;92mpassagem\033[m custará \033[1;92m{}\033[mR$'.format(preço))
elif km > 200:
    preço = km * 0.45
    print('Sua \033[1;92mpassagem\033[m custará \033[1;92m{}\033[mR$'.format(preço))
print('\033[4;94mObrigado pela preferência!!!\033[m')