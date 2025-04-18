print('===')
print('\033[4m999\033[m')
print('===')
c = 0
s = 0
n2 = int(input('Digite um valor qualquer (inteiro; digite \033[4m999\033[m para parar): '))
while n2 != 999:
        c += 1
        s += n2
        n2 = int(input('Digite outro valor qualquer (inteiro): '))
print('.')
print('O número de valores digitados até o \033[4m999\033[m (exceto o \033[4m999\033[m) foi {}.'.format(c))
print('A soma de todos os valores digitados até o \033[4m999\033[m (exceto o \033[4m999\033[m) é {}.'.format(s))

