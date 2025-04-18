print('-=-'*7)
print('\033[4;37mTABUADA REMASTERIZADA\033[m')
print('-=-'*7)
val = int(input('Escolha um valor para analisarmos a \033[4;37mtabuada\033[m: '))
for c in range(1, 11):
    p = val * c
    print('{} X {} = {}'.format(val, c, p))