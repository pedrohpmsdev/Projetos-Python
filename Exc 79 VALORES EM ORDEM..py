print('-=-'*6)
print(' VALORES EM ORDEM')
print('-=-'*6)
c = 1
lista = list()
while True:
    n = int(input(f'Digite o {c}º valor: '))
    c += 1
    if n in lista:
        print('Valores duplicados não serão adicionados.')
    else:
        lista.append(n)
    res = input('Quer cotinuar?[S]/[N]: ').upper().strip()[0]
    while res not in 'NS':
        print('Valor inválido. Digite novamente.')
        res = input('Quer cotinuar?[S]/[N]: ').upper().strip()[0]
    if res == 'N':
        break
lista.sort()
print(f'Sua lista ficou assim: {lista}.')