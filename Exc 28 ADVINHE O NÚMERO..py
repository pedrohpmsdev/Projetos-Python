from random import choice
from time import sleep
print('-'*17)
print('\033[4mADIVINHE UM \033[4;91mNÚMERO\033[m')
print('-'*17)
l = [1,2,3,4,5]
n = choice(l)
res = int(input('Entre \033[4;91m1\033[m e \033[4;91m5\033[m, tente advinhar o \033[4;91mnúmero\033[m que eu \033[1;94mpensei\033[m: '))
print('PROCESSANDO...')
sleep(3)
if res == n:
    print('\033[1;93mUAU\033[m, você é um \033[1;93mexímio advinho\033[m! \033[1;92mParabéns\033[m, você \033[1;92macertou\033[m!')
elif res > 5 or res < 1:
    print('Os valores que eu posso ter pensado estão entre \033[4;91m1\033[m e \033[4;91m5\033[m. \033[4;91m{}}\033[m não está entre eles.'.format(res))
else:
    print('Que pena... Você \033[1;91merrou\033[m! Eu \033[1;95mpensei\033[m em \033[1;91m{}\033[m.'.format(n))