print('=-'*8)
print('QUAL O SEU \033[4mNOME\033[m?')
print('=-'*8)
n = input('Qual é o seu \033[4mnome completo\033[m? ').strip().split()
print('\033[1;93mPRIMEIRO NOME\033[m: \033[1;93m{}\033[m'.format(n[0]))
print('\033[1;93mPRIMEIRO NOME\033[m: \033[1;93m{}\033[m'.format(n[-1]))
