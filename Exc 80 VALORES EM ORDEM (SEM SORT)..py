print('-=-'*5)
print('ORDEM SEM SORT')
print('-=-'*5)
lista = list()
for c in range (0, 5):
    n = int(input(f'Digite o {c+1}º valor: '))
    if c == 0:
        maior = n
        lista.append(n)
    else:
        for p in range(0, len(lista)):
            if n >= maior:
                maior = n
                lista.append(n)
                print('Adicionado ao fim da lista.')
                break
            if n < lista[p]:
                lista.insert(p, n)
                print(f'Adicionado na posição {p} da lista.')
                break
print(f'Lista: \033[1;95m{lista}\033[m.')
