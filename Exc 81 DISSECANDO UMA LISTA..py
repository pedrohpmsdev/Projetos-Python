print('-=-'*7)
print('DISSECANDO UMA LISTA')
print('-=-'*7)
lista = list()
tem5 = c = 0
while True:
    c += 1
    n = int(input(f'Digite o {c}º valor: '))
    lista.append(n)
    if n == 5:
        tem5 = 1
    res = input('Quer continuar? [S]/[N]: ').strip().upper()[0]
    while res not in 'NS':
        print('Resposta inválida. Tente novamente.')
        res = input('Quer continuar? [S]/[N]: ').strip().upper()[0]
    if res == 'N':
        break
qnt = len(lista)
lista.sort(reverse = True)
print(f'O número de elementos na lista é: \033[1;93m{qnt}\033[m.')
print(f'A lista em ordem decrescente: \033[1;93m{lista}.\033[m')
if tem5 == 1:
    print(f'Existe um 5 na lista na posição \033[1;93m', end='')
    for p, c in enumerate(lista):
        if c == 5:
            print(f'[{p}] ', end='')
    print('\033[m.')
else:
    print(f'Não existe um 5 na lista.')
