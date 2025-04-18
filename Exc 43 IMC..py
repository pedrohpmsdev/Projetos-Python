print('=-='*8)
print('ÍNDICE DE MASSA CORPORAL')
print('=-='*8)
m = float(input('Qual sua massa corporal(kg)? '))
a = float(input('Qual sua altura(m)? '))
imc = m/a**2
if imc <= 18.5:
    print('Você está na categoria: \033[1;93mAbaixo do peso\033[m, com IMC = {}.'.format(imc))
elif 25 > imc > 18.5:
    print('Você está na categoria: \033[1;92mPeso ideal\033[m, com IMC = {}.'.format(imc))
elif 30 > imc >= 25:
    print('Você está na categoria: \033[1;93mSobrepeso\033[m, com IMC = {}.'.format(imc))
elif 40 > imc >= 30:
    print('Você está na categoria: \033[1;93mObesidade\033[m, com IMC = {}.'.format(imc))
elif imc >= 40:
    print('Você está na categoria: \033[1;91mObesidade mórbida\033[m, com IMC = {}.'.format(imc))