print('-'*19)
print('VALORES POR EXTENSO')
print('-'*19)
numbers = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
           'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
           'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
           'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito',
           'Dezenove', 'Vinte')
while True:
    valor = int(input('Digite um valor entre 0 e 20: '))
    if 20 >= valor >= 0:
        print(f'O valor digitado foi o \033[4m{numbers[valor]}\033[m.')
        res = input('Quer continuar [S]/[N]?').strip().upper()[0]
        while res not in 'SN':
            print('Resposta inválida. Tente novamente.')
            res = input('Quer continuar [S]/[N]?').strip().upper()[0]
        if res == 'N':
            break