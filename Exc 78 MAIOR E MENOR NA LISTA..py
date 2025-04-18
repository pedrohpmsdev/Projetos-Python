print('-'*17)
print('\033[4mLISTA MAIOR/MENOR\033[m')
print('-'*17)
maior = menor = 0
lista = list()
for p in range(0,5):
    lista.append(int(input(f'Digite o {p+1}o valor: ')))
    if p == 0:
        maior = menor = lista[p]
    elif lista[p] > maior:
        maior = lista[p]
    elif lista[p] < menor:
        menor = lista[p]
print(f'O MAIOR VALOR DIGITADO: {maior}; NA POSIÇÃO: ',end='')
for ps, c in enumerate(lista):
    if c == maior:
        print(f'{ps}; ',end='')
print(f'\nO MENOR VALOR DIGITADO: {menor}; NA POSIÇÃO: ',end='')
for ps, c in enumerate(lista):
    if c == menor:
        print(f'{ps}; ', end='')