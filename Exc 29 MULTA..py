print('#*#*#')
print('\033[1;93mMULTA\033[m')
print("#*#*#")
vel = float(input('Qual \033[1;91mvelocidade máxima\033[m seu carro atingiu? '))
if vel > 80:
    print('Seu carro atingiu \033[1;91m{}\033[mkm/h. Por ter \033[1;91multrapassado\033[m o \033[1;94mlimite\033[m de \033[1;94m80km/h\033[m, você será \033[1;93mmultado\033[m por \033[1;91m{}\033[mR$.'.format(vel, vel*7))
else:
    print('Seu carro atingiu \033[1;91m{}\033[mkm/h. Por ter não ter \033[1;91ultrapassado\033[m o \033[1;94mlimite\033[m de \033[1;94m80km/h\033[m, você \033[4mnão\033[m será \033[1;93mmultado\033[m.'.format(vel))
