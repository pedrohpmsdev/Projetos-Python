from random import sample
maior = menor = 0
print('='*16)
print('\033[1;95mGERADOR DE TUPLA\033[m')
print('='*16)
gerador = input('\033[1;95mVamos gerar uma tupla? Digite qualquer coisa, pressione [ENTER] e veja a máxima ocorrer! \033[m')
tupla = sample(range(1, 100), k = 5)
print(f'A tupla gerada foi: \033[1;95m{tupla}\033[m.')
for c in range(0, 5):
    if c == 0:
        maior = tupla[0]
        menor = tupla[0]
    else:
        if tupla[c] > maior:
            maior = tupla[c]
        elif tupla[c] < menor:
            menor = tupla[c]
print(f'O maior valor foi \033[1;95m{maior}\033[m.')
print(f'O menor valor foi \033[1;95m{menor}\033[m.')

#Poderia fazer assim também (mas eu prefiro com sample):
#tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
#Como estão entre parênteses, configura uma tupla.

#OUTRO JEITO DE FAZER MAIOR E MENOR EM TUPLAS:
#print(f'O maior valor sorteado foi {max(tupla)}
#print(f'O menor valor sorteado foi {min(tupla)}

