print('-'*19)
print('\033[1;94mTONINHO ELETRÔNICOS\033[m')
print('-'*19)
prd = float(input('Qual o \033[1;92mpreço\033[m do produto? '))
pg = int(input("""Qual a \033[1;95mforma de pagamento\033[m?
   - À VISTA NO DINHEIRO/CHEQUE [1];
   - À VISTA NO CARTÃO [2];
   - EM ATÉ 2X NO CARTÃO [3];
   - 3X OU MAIS NO CARTÃO [4].
   """))
if pg == 1:
    desc = prd * 0.9
    print('Você terá um \033[1;92mdesconto de 10%\033[m, pagando {}R$.'.format(desc))
elif pg == 2:
    desc = prd *0.95
    print('Você terá um \033[1;92mdesconto de 5%\033[m, pagando {}R$.'.format(desc))
elif pg == 3:
    print('Você não terá desconto, pagando {}R$.'.format(prd))
elif pg == 4:
    j = prd * 1.20
    print('Você terá um \033[1;91mjuros de 20% no preço total\033[m, pagando {}R$.'.format(j))
