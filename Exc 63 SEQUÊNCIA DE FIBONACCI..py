print('=-'*11)
print('\033[1;95mSEQUÊNCIA DE FIBONACCI\033[m')
print('=-'*11)
t1 = 0
t2 = 1
t3 = 0
c = 1
mais = 1
termos = int(input('Quantos termos você quer ver da \033[1;95mSequência de Fibonacci\033[m? '))
print('{} '.format(t1), end = '')
total = termos
while mais != 0:
    total += mais
    while c < total:
        print('{} '.format(t2), end = '')
        t3 = t1
        t1 = t2
        t2 = t3 + t1
        c += 1
    print('-> FIM')
    mais = int(input('Quer ver mais quantos termos? '))
print('Finalizando o programa...')
print('Programa finalizado.')
