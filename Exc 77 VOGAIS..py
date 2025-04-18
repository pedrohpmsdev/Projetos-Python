print('=='*3)
print('\033[4mVOGAIS\033[m')
print('=='*3)
palavras = ('Pedro', 'Henrique', 'Pinto', 'Mota', 'Simoes', 'Salvador', 'Bahia',
            'UFBA', 'Itaigara', 'Idosas')
for c in palavras:
    print(f'\nAs vogais em \033[4;91m{c.upper()}\033[m são: ', end='')
    for p in c:
        if p in 'AaEeIiOoUu':
            print(f'\033[4;91m{p.upper()}\033[m; ', end='')