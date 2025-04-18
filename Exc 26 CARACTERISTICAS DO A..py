print('-='*10)
print('\033[1;94mCARACTERÍSTICAS DO A\033[m')
print('-='*10)
frase = input('Digite uma \033[4mfrase\033[m ou uma \033[4mpalavra\033[m qualquer: ').strip().lower()
print('QUANTIDADE DE LETRAS "\033[1;94mA\033[m": \033[1;94m{}\033[m'.format(frase.count('a')))
print('POSIÇÃO DA PRIMEIRA LETRA "\033[1;94mA\033[m": \033[1;94m{}\033[m'.format(frase.find('a')+ 1))
print('POSIÇÃO DA ÚLTIMA LETRA "\033[1;94mA\033[m": \033[1;94m{}\033[m'.format(frase.rfind('a') + 1))


