print('='*10)
print('TRIÂNGULOS')
print('='*10)
l1 = float(input('Qual o valor do \033[1;91mprimeiro lado\033[m?: '))
l2 = float(input('Qual o valor do \033[1;91msegundo lado\033[m?:'))
l3 = float(input('Qual o valor do \033[1;91mteceiro lado\033[m?:'))

if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    print('\033[1;92mIsso é um triângulo!\033[m')
    if l1 != l2 != l3:
        print('Isso é um \033[1;95mtriângulo escaleno (3 lados diferentes)\033[m.')
    elif l1 == l2 != l3 or l1 == l3 != l2 or l2 == l3 != l1:
        print('Isso é um \033[1;95mtriângulo isósceles (2 lados iguais)\033[m.')
    elif l1 == l2 == l3:
        print('Isso é um \033[1;95mtriângulo equilátero (3 lados iguais)\033[m.')
else:
    print('\033[1;91mIsso não é um triângulo.\033[m')

