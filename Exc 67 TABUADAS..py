print('-'*8)
print('TABUADAS')
print('-'*8)
while True:
    tab = int(input('Você quer ver a tabuada de qual número (se não quiser, digite um valor negativo)? '))
    if tab < 0:
        break
    print('-=-'*5)
    for c in range(1, 11):
        mult = tab*c
        print(f'  {tab} X {c} = {mult}.')
    print('-=-'*5)
print('-=-'*7)
print('TABUADAS FINALIZADAS!')

