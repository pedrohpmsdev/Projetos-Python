print('='*16)
print('\033[1;96mCAIXA ELETRÔNICO\033[m')
print('='*16)
valor = int(input('Qual valor você quer sacar? '))
rest50 = rest20 = rest10 = 0
if (valor // 50) > 0:
    n50 = valor // 50
    print(f'Você precisará de {n50} cédulas de 50R$.')
rest50 = valor % 50
if (rest50 // 20) > 0:
    n20 = rest50 // 20
    print(f'Você precisará de {n20} cédulas de 20R$.')
rest20 = rest50 % 20
if (rest20 // 10) > 0:
    n10 = rest20 // 10
    print(f'Você precisará de {n10} cédulas de 10R$.')
rest10 = rest20 % 10
if (rest10 // 1) > 0:
    print(f'Você precisará de {rest10} cédulas de 1R$.')
print('=-='*10)
print('FIM DO SAQUE. ATÉ A PRÓXIMA!')


