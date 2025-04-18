print('-=-'*8)
print('\033[1;94mAPROVAÇÃO DE EMPRÉSTIMO\033[m')
print('-=-'*8)
print('0lá, Bom dia! Sou a \033[1;94mIA do Banco do Brasil\033[m e estou aqui para avaliar \033[1;96mempréstimos para casas\033[m. Vamos iniciar o \033[1;95mprocesso de avaliação\033[m: ')
nome = input('Seu \033[1;92mnome completo\033[m: ')
sal = float(input('Seu \033[1;92msalário atual\033[m: '))
val = float(input('O \033[1;92mvalor da casa\033[m: '))
temp = int(input('Quanto \033[4;37mtempo\033[m durará o pagamento (em anos): '))
prest: float = val/(temp*12)
if prest > (sal*0.3):
    print('\033[1;91mEMPRÉSTIMO NEGADO\033[m. Você pagaria uma prestação mensal de \033[1;92m{:.2f}\033[mmR$.'.format(prest))
elif prest <= (sal*0.3):
    print('\033[1;92mEMPRÉSTIMO APROVADO\033[m. Você pagará uma prestação mensal de \033[1;92m{:.2f}\033[mmR$.'.format(prest))



