print('-=-'*4)
print('\033[4mIDADE E SEXO\033[m')
print('-=-'*4)
maioridade = homens = mulheresmenores = 0
while True:
    idade = int(input('Qual sua idade? '))
    sexo = input('Qual seu sexo(M/F)?').strip().upper()[0]
    while sexo not in 'MF':
        print('Resposta inválida. Tente novamente.')
        sexo = input('Qual seu sexo(M/F)?').strip().upper()[0]
    if idade >= 18:
        maioridade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade <= 20:
        mulheresmenores += 1
    res = input('Quer continuar [S]/[N]? ').strip().upper()[0]
    if res == 'N':
        break
    while res not in 'NS':
        print('Resposta inválida. Tente novamente.')
        res = input('Quer continuar [S]/[N]? ').strip().upper()[0]
print(f'O número de pessoas com mais de 18 anos é igual a {maioridade}.')
print(f'O número de homens cadastrados é igual a {homens}.')
print(f'O número de mulheres com menos de 20 anos é igual a {mulheresmenores}.')