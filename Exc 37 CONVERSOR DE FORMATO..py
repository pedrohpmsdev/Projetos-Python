
print('-='*10)
print('\033[1;37mCONVERSOR DE FORMATO\033[m')
print('-='*10)
red = '\033[1;91m'
fim = '\033[m'
gray = '\033[1;37m'
n = int(input('Qual \033[1;91mnúmero\033[m você quer converter? '))
f = int(input("""Para qual \033[1;37mformato\033[m você quer converter?
  - \033[1;37mBINÁRIO\033[m [1];
  - \033[1;37mOCTAL\033[m [2];
  - \033[1;37mHEXADECIMAL\033[m [3]. """))
if f == 1:
    print('{}{}{} em {}Binário{}: {}.'.format(red, n, fim, gray, fim, bin(n)[2:]))
elif f == 2:
    print('{}{}{} em {}Octal{}: {}.'.format(red, n, fim, gray, fim, oct(n)[2:]))
elif f == 3:
    print('{}{}{} em {}Hexadecimal{}: {}.'.format(red, n, fim, gray, fim, hex(n)[2:]))
else:
    print('{}RESPOSTA INVÁLIDA{}. Reinicie o programa e digite 1, 2 ou 3.'.format(red, fim))