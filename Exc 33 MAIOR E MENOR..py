print('='*13)
print('MAIOR E MENOR')
print('='*13)
n1 = float(input('Digite o \033[4mprimeiro valor\033[m: '))
n2 = float(input('Digite o \033[4msegundo valor\033[m: '))
n3 = float(input('Digite o \033[4mterceiro valor\033[m: '))
maior: float = n1
menor: float = n1

if n2 > maior:
    maior = n2
elif n2 < menor:
    menor = n2
if n3 > maior:
    maior = n3
elif n3 < menor:
    menor = n3
if maior == menor:
    print('O \033[4mmaior valor\033[m e o \033[4mmenor valor\033[mm são \033[4;93miguais\033[m, sendo o \033[4m{}\033[m.'.format(maior))
    breakpoint()

print('\033[4mMAIOR VALOR\033[m: \033[4m{}\033[m.'.format(maior))
print('\033[4mMENOR VALOR\033[m: \033[4m{}\033[m.'.format(menor))
