print('-'*22)
print('LISTA, PARES E ÍMPARES')
print('-'*22)
c = 0
lista = list()
listapares = list()
listaimpares = list()
while True:
    c += 1
    n = int(input(f'Digite o {c}º valor: '))
    lista.append(n)
    if n % 2 == 0:
        listapares.append(n)
    elif n % 2 == 1:
        listaimpares.append(n)
    res = input('Quer continuar? [S]/[N]: ').strip().upper()[0]
    while res not in 'SN':
        print('Resposta inválida. Tente novamente.')
        res = input('Quer continuar? [S]/[N]: ').upper().strip()[0]
    if res == 'N':
        break
print(f'LISTA COMUM: \033[1;94m{lista}\033[m')
print(f'LISTA DE PARES: \033[1;94m{listapares}\033[m')
print(f'LISTA DE ÍMPARES: \033[1;94m{listaimpares}\033[m')
