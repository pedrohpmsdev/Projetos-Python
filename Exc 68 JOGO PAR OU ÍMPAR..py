from random import choice
print('-'*17)
print('\033[4mJOGO PAR OU ÍMPAR\033[m')
print('-'*17)
lista = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
esc = choice(lista)
vit = 0
while True:
    esc = choice(lista)
    print('-=-' * 7)
    pi = input('Você quer par ou ímpar [P]/[I]? ').upper().strip()[0]

    while pi != 'P' and pi != 'I':
        print('Resposta inválida. Tente novamente.')
        pi = input('Você quer par ou ímpar [P]/[I]? ').upper().strip()[0]

    n = int(input('Você vai jogar qual valor(entre 1 e 10)? '))
    s = n + esc
    print(f'Você jogou \033[4m{n}\033[m e o computador jogou \033[4m{esc}\033[m, sendo o resultado \033[4m{s}\033[m.')
    if pi == 'P':
        if s % 2 == 0:
            print('Deu PAR.')
            print('Você venceu!!! Vamos jogar novamente.')
            vit += 1
        elif s % 2 == 1:
            print('Deu ÍMPAR.')
            print('O computador venceu. Fim de jogo.')
            break
    if pi == 'I':
        if s % 2 == 0:
            print('Deu PAR.')
            print('O computador venceu. Fim de jogo.')
            break
        if s % 2 == 1:
            print('Deu ÍMPAR.')
            print('Você venceu!!! Vamos jogar novamente')
            vit += 1
print('-=-'*7)
if vit == 1:
    print(f'Você venceu um total de \033[4m{vit}\033[m rodada!')
elif vit == 0:
    print(f'Você venceu um total de \033[4m{vit}\033[m rodadas.')
else:
    print(f'Você venceu um total de \033[4m{vit}\033[m rodadas seguidas.')

