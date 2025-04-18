from sys import prefix

print('='*8)
print('\033[1;92mDESCONTO\033[m')
print('='*8)
pre = float(input('Quanto você vai \033[1;92mpagar\033[m? '))
des = pre*0.95
print('Deu \033[1;93msorte\033[m! Esse valor de \033[1;92m{}\033[m concede um desconto de \033[4;91m5%\033[m na sua compra! Agora você pagará \033[4;91m{}\033[m'.format(pre, des))