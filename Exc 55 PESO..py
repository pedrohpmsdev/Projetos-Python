print('-'*5)
print('\033[1;93mPESOS\033[m')
print('-'*5)
maior = 0
menor = 0
for c in range(0,5):
    peso = float(input('Qual o peso da {}ª pessoa? '.format(c+1)))
    if c == 0:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('A pessoa mais pesada pesa \033[1;91m{}Kg\033[m.'.format(maior))
print('A pessoa mais leve pesa \033[1;96m{}Kg\033[m.'.format(menor))