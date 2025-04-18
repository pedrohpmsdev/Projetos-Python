print('-=-'*7)
print('\033[1;92mVALIDADE DE EXPRESSÃO\033[m')
print('-=-'*7)
exp = input('Digite uma expressão matémática: ')
pilha = []
for c in exp:
    if c == '(':
        pilha.append('(')
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida.')

