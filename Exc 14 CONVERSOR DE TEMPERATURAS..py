print('='*25)
print('\033[1;96mCONVERSOR\033[m DE \033[1;91mTEMPERATURAS\033[m')
print('='*25)
c = float(input('Quantos \033[1;37mgraus\033[m está fazendo(em \033[1;91mCelsius\033[m)? '))
f = c*1.8 + 32
print('\033[1;91m{}ºC\033[m equivalem a \033[1;96m{}ºF\033[m.'.format(c, f))