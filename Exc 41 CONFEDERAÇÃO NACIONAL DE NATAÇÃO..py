from datetime import date
print('-'*32)
print('\033[1;96mCONFEDERAÇÃO NACIONAL DE NATAÇÃO\033[m')
print('-'*32)
nasc = int(input('Em qual ano você nasceu? '))
atual = date.today().year
idade = atual - nasc
if idade <= 9:
    print('Você está na categoria: \033[1;95mMIRIM\033[m.')
elif 14 >= idade >= 10:
    print('Você está na categoria: \033[1;95mINFANTIL\033[m.')
elif 19 >= idade >= 15:
    print('Você está na categoria: \033[1;95mJÚNIOR\033[m.')
elif 25>= idade >= 20:
    print('Você está na categoria: \033[1;95mSÊNIOR\033[m.')
elif idade > 25:
    print('Você está na categoria: \033[1;95mMASTER\033[m.')