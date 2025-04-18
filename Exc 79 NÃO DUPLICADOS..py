print('-=-'*5)
print('\033[1;91mNÃO DUPLICADOS!\033[m')
print('-=-'*5)
valores = list()
while True:
    v = int(input('Quer adicionar qual valor?: '))
    if v in valores:
        print('Valores duplicados não serão válidos! Retirando a duplicata...')
    else:
        valores.append(v)
    res = input('Quer continuar?[S]/[N]: ').upper().strip()[0]
    while res not in 'NS':
        print('Resposta inválida. ',end='')
        res = input('Quer continuar?[S]/[N]: ').upper().strip()[0]
    if res == 'N':
        break
valores.sort()
print(f'A sua lista ficou assim: {valores}.')