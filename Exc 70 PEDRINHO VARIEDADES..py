print('-'*19)
print('\033[4;93mPEDRINHO VARIEDADES\033[m')
print('-'*19)
total = n1000 = n = 0
barato = ''
while True:
    nome = input('Nome do produto: ')
    preco = float(input('Preço do produto: '))
    total += preco
    n += 1
    if n == 1:
        barato = nome
    elif nome < barato:
        barato = nome
    if preco >= 1000:
        n1000 += 1
    res = ' '
    while res not in 'SN':
        res = input('Quer continuar [S]/[N]? ').strip().upper()[0]
    if res == 'N':
        break
print(f'O \033[4;92mtotal da compra\033[m foi de \033[4;92m{total}\033[mR$.')
print(f'O número de produtos que \033[1;91mcustaram mais de 1000 reais\033[m foi \033[1;91m{n1000}\033[m.')
print(f'O produto \033[1;96mmais barato\033[m foi \033[1;96mo(a) {barato}\033[m.')