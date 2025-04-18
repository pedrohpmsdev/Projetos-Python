print('=====')
print('BREAK')
print('=====')

cont = 0
s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'O número de valores é {cont}.')
print(f'A soma dos valores é {s}.')
