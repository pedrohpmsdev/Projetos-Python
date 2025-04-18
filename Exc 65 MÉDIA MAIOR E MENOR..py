print('='*20)
print('MÉDIA, MAIOR E MENOR')
print('='*20)
s = 0
c = 0
n = float(input('Digite um valor: '))
maior = menor = n
s += n
c += 1
res = input('Quer continuar? [S]/[N]').upper()
while res == 'S':
    n = float(input('Digite um valor: '))
    s += n
    c += 1
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    res = input('Quer continuar? [S]/[N]').upper()
if res != 'S' and res != 'N':
    while res != 'S' and res != 'N':
        print('Resposta inválida, tente novamente.')
        res = input('Quer continuar? [S]/[N]').upper()
media = s/c
print('A \033[1;91mmédia\033[m entre os valores lidos é igual a \033[1;91m{}\033[m.'.format(media))
print('O \033[1;91mmaior\033[m valor lido foi o \033[1;91m{}\033[m.'.format(maior))
print('O \033[1;91mmenor\033[m valor lido foi o \033[1;91m{}\033[m.'.format(menor))
