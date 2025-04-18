print('='*22)
print('MAIOR E MENOR NA LISTA')
print('='*22)
c = 0
maior = menor = 0
lista = list()
while c < 5:
    lista.append(int(input('Digite um valor: ')))
    if c == 0:
        maior = menor = lista[c]
    elif lista[c] > maior:
        maior = lista[c]
    elif lista[c] < menor:
        menor = lista[c]
    c += 1
print(f'\033[1;91mMAIOR: {maior}.\033[m Suas posições: ', end='')
for c in range(0, 5):
    if lista[c] == maior:
        print(f'{c}; ')
print(f'\033[1;91mMENOR: {menor}.\033[m Suas posições: ', end='')
for c in range(0, 5):
    if lista[c] == menor:
        print(f'{c}; ', end='')
