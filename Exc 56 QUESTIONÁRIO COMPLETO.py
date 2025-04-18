print('-=-'*4)
print('QUESTIONÁRIO')
print('-=-'*4)
soma = 0
totmulher = 0
noemaior = 0
maior = 0
for c in range(0,4):
    nome = input('Qual o nome da {}ª pessoa? '.format(c+1)).strip()
    idade = int(input('Quantos anos tem a {}ª pessoa? '.format(c+1)))
    sexo = input('Qual o sexo da {}ª pessoa [M]/[F]? '.format(c+1)).upper().strip()
    soma += idade
    if c == 0 and sexo == 'M':
        maior = idade
    if idade > maior and sexo == 'M':
        maior = idade
        nomemaior = nome
    if sexo == 'F' and idade <= 20:
        totmulher += 1
media = soma/4
print('A \033[1;93mmédia\033[m das idades é igual a \033[1;93m{}\033[m.'.format(media))
print('O \033[1;92mnome\033[m do homem mais velho é \033[1;92m"{}"\033[m.'.format(nomemaior))
print('O \033[1;95mnúmero\033[m de mulheres com 20 anos ou menos é igual a \033[1;95m{}\033[m.'.format(totmulher))
