print('\033[1;93;107m=\033[m'*20)
print('\033[1;93;107mCONVERSOR DE MEDIDAS\033[m')
print('\033[1;93;107m=\033[m'*20)
m = float(input('Quantos metros você deseja converter? '))

km = m/1000
hm = m/100
dam = m/10
dc = m*10
c = m*100
mi = m*1000
print('{} metros em \033[7;97;101mmilímetros: {}cm\033[m'.format(m, mi))
print('{} metros em \033[7;97;101mcentímetros: {}mm\033[m'.format(m, c))
print('{} metros em \033[7;97;101mdecímetros: {}mm\033[m'.format(m, dc))
print('{} metros em \033[7;97;101mdecâmetros: {}mm\033[m'.format(m, dam))
print('{} metros em \033[7;97;101mhectômetros: {}mm\033[m'.format(m, hm))
print('{} metros em \033[7;97;101mquilômetros: {}mm\033[m'.format(m, km))
