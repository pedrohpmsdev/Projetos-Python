from random import random, choice
print('-'*17)
print('\033[1;93mSORTEIO DE ALUNOS\033[m')
print('-'*17)
n1 = input('Qual o nome do \033[1;94mprimeiro aluno?\033[m ')
n2 = input('Qual o nome do \033[1;94msegundo aluno?\033[m ')
n3 = input('Qual o nome do \033[1;94mterceiro aluno?\033[m ')
n4 = input('Qual o nome do \033[1;94mquarto aluno?\033[m ')
op = [n1, n2, n3, n4]
re = choice(op)
print('O \033[1;94maluno\033[m \033[1;92mescolhido\033[m para \033[1;37mapagar\033[m o quadro foi \033[1;94m{}\033[m'.format(re))
