print('-=-'*8)
print('ORDEM CRESCENTE\033[1;91m(SEM SORT)\033[m')
print('-=-'*8)
valores = list()
for c in range(0,5):
    v = int(input(f'Digite o {c+1}º valor: '))
    if c == 0 or v > valores[-1]:
        valores.append(v)
    else:
        p = 0
        while p < len(valores):
            if v <= valores[p]:
                valores.insert(p, v)
                break
            p += 1
print(f'LISTA DE VALORES: {valores}.')
