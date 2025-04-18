print('='*16)
print(' TOCANDO ÁUDIOS')
print('='*16)
import pygame
pygame.init()
pygame.mixer.music.load('Quem-escreve-e-apaga-depois.wav')
pygame.mixer.music.play()
input()
pygame.event.wait()

'''FAZER UM DESSE COM VÁRIOS ÁUDIOS QUANDO VER IF OU SWITCH CASE'''

