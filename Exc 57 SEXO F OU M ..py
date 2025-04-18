print('\033[1;95m-\033[m\033[1;91m=\033[m'*4)
print('\033[1;95mF\033[m ou \033[1;91mM\033[m??')
print('\033[1;95m-\033[m\033[1;91m=\033[m'*4)

res = str(input('Qual o seu sexo [M]/[F]? ')).upper()[0].strip()
while res != 'M' and res != 'F':
    res = input('Resposta Inválida. Por favor, informe seu sexo [M]/[F]: ').upper()[0].strip()
print('Sexo {} registrado com sucesso!'.format(res))

#poderia ter feito assim: while res not in 'MF': (repete o while se 'res' não estiver em 'MF', ou seja, se não for M ou F)

