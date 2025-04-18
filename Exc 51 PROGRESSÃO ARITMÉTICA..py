print('-=-'*7)
print('PR0GRESSÃ0 ARITMÉTICA')
print('-=-'*7)
p = int(input('Digite o \033[1;95mPRIMEIRO TERMO\033[m da PA: '))
r = int(input('Digite a \033[1;95mRAZÃO\033[m da PA: '))
z = r * 10 + p
for c in range (p, z, r):
    print (c,end=' -> ')
print('FINALIZADA!')
