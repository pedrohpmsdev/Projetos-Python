print('-=-'*6)
print('\033[1;92mTABELA BRASILEIRÃO\033[m')
print('-=-'*6)
tabela = ('BOTAFOGO', 'PALMEIRAS', 'FLAMENGO', 'FORTALEZA', 'INTERNACIONAL',
          'SÃO PAULO', 'CORINTHIANS', 'BAHIA', 'CRUZEIRO', 'VASCO DA GAMA',
          'EC VITÓRIA', 'ATLÉTICO-MG', 'FLUMINENSE', 'GRÊMIO', 'JUVENTUDE',
          'BRAGANTINO', 'ATHLETICO-PR', 'CRÍCIUMA', 'ATLÉTICO-GO', 'CUIABÁ')
print(f'Os \033[4;92m5 primeiros colocados\033[m foram: {tabela[:5]}.')
print(f'Os \033[4;91m4 lanternas\033[m foram: {tabela[-4:]}')
print(f'A lista com os times em \033[4mordem alfabética\033[m: {sorted(tabela)}')
print(f'A posição do \033[1;91mEC Vitória\033[m foi: \033[4m{tabela.index('EC VITÓRIA')+1}º lugar\033[m.')
