l = 'LISTAGEM DE PREÇOS'
print('-'*38)
print('{:^38}'.format(l))
print('-'*38)
cont = 0
lista = ('Notebook Lenovo LOQ', 4299.90,'Notebook Acer Nitro V-15', 4799.90, 'Mesa Digitalizadora Wacom', 189.90,
         'Garmin Forehunner 235', 1499.90, 'Iphone 11 Branco', 2499.90, 'T-Dagger Bora',
         199.90, 'Raquete elétrica Lidermix', 29.90, 'Luminária Pixar articulada', 79.90, 'Ventilador ARNO', 249.90)
for c in lista:
    if cont % 2 == 0:
        print('{:.<29}R$ '.format(c), end='')
    if cont % 2 == 1:
        print('{:>6}'.format(c))
    cont += 1
print('-'*38)