from math import sqrt
print('\033[1;91m=-=\033[m'*7)
print('\033[1;91mTEOREMA DE PITÁGORAS\033[m')
print('\033[1;91m=-=\033[m'*7)
co = float(input('Medida do \033[1;91mCateto Oposto\033[m(m): '))
ca = float(input('Medida do \033[1;91mCateto Adjacente\033[m(m): '))
h = co**2 + ca**2
print('A \033[1;94mHipotenusa\033[m mede \033[1;94m{:.2f}\033[mm.'.format(sqrt(h)))
