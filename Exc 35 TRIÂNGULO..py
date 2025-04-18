print('-=-'*5)
print('\033[4;93mÉ UM TRIÂNGULO?\033[m')
print('-=-'*5)
l1 = float(input('Diga o \033[1;92mvalor do LADO A\033[m do \033[1;93msuposto triângulo\033[m: '))
l2 = float(input('Diga o \033[1;92mvalor do LADO B\033[m do \033[1;93msuposto triângulo\033[m: '))
l3 = float(input('Diga o \033[1;92mvalor do LADO C\033[m do \033[1;93msuposto triângulo\033[m: '))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print ('O \033[1;93msuposto triângulo\033[m \033[1;92mABC\033[m, com \033[1;92mA = {}, B = {}, C = {}\033[m, é realmente um \033[1;93mautêntico triângulo\033[m!'.format(l1, l2, l3))
else:
    print ('O \033[1;93msuposto triângulo\033[m \033[1;92mABC, com A = {}, B = {}, C = {}\033[m, é uma \033[1;91mfarsa\033[m! \033[1;91mNão é um triângulo\033[m.'.format(l1, l2, l3))
