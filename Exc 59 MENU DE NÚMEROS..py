from time import sleep

print('\033[1;91m-\033[m'*15)
print('\033[1;91mMENU DE NÚMEROS\033[m')
print('\033[1;91m-\033[m'*15)

n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
select = 0
while select != 5:
    select = int(input("""Selecione uma opção:
     - SOMAR \033[1;91m[1]\033[m;
     - MULTIPLICAR \033[1;91m[2]\033[m;
     - MAIOR \033[1;91m[3]\033[m;
     - NOVOS NÚMEROS \033[1;91m[4]\033[m;
     - SAIR DO PROGRAMA \033[1;91m[5]\033[m. """))
    if select == 1:
        soma = n1 + n2
        print('{} + {} = {}.'.format(n1, n2, soma))
    elif select == 2:
        multi = n1 * n2
        print('{} X {} = {}.'.format(n1, n2, multi))
    elif select == 3:
        if n1 > n2:
            print('O maior entre {} e {} é o {}.'.format(n1, n2, n1))
        else:
            print('O maior entre {} e {} é o {}.'.format(n1, n2, Fqn2))
    elif select == 4:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
    elif select == 5:
        print('Saindo do programa...')
    elif select > 5 or select < 1:
        print('Seleção inválida. Tente novamente.')
    sleep(1)
    print('---------||---------')
print('FINALIZADO!')