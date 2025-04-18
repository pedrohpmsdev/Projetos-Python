from math import sin, cos, tan, radians
print('=-='*5)
print(' \033[1;94mSEN COS E TAN\033[m')
print('=-='*5)
a = int(input('Digite o valor de um \033[1;95mângulo\033[m qualquer: '))

print('\033[1;94mSeno\033[m de \033[1;95m{}\033[m = \033[1;94m{:.2f}\033[m.'.format(a, sin(radians(a))))
print('\033[1;94mCosseno\033[m de \033[1;95m{}\033[m = \033[1;94m{:.2f}\033[m'.format(a, cos(radians(a))))
print('\033[1;94mTangente\033[m de \033[1;95m{}\033[m = \033[1;94m{:.2f}\033[m'.format(a, tan(radians(a))))
