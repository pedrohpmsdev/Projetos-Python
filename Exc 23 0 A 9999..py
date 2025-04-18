print('*'*8)
print('O a 9999')
print('*'*8)
n = int(input('Digite um \033[1;91mnúmero\033[m e iremos analisar suas \033[1;95mordens\033[m: '))
u = n % 10
d = (n // 10) % 10
c = (n // 100) % 10
m = n // 1000

print('\033[1;95mUNIDADE\033[m: \033[1;91m{}\033[m'.format(u))
print('\033[1;95mDEZENA\033[m: \033[1;91m{}\033[m'.format(d))
print('\033[1;95mCENTENA\033[m: \033[1;91m{}\033[m'.format(c))
print('\033[1;95mMILHAR\033[m: \033[1;91m{}\033[m'.format(m))

