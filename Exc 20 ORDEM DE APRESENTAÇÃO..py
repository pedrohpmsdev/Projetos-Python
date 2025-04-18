print('=-='*5)
print('\033[1;94mSORTEIO DA ORDEM\033[m')
print('=-='*5)
from random import sample
n1 = input('Qual o nome do \033[1;96mprimeiro aluno?\033[m ')
n2 = input('Qual o nome do \033[1;96msegundo aluno?\033[m ')
n3 = input('Qual o nome do \033[1;96mterceiro aluno?\033[m ')
n4 = input('Qual o nome do \033[1;96mquarto aluno?\033[m ')
op = [n1, n2, n3, n4]
es = sample(op, k=4)
print('\033[1;94mOrdem das apresentações: {}\033[m'.format(es))
'''Ou random.suffle(op), isso embaralha a lista. Depois é só print(op)'''