import pygame

pygame.init()
pygame.mixer.music.load('Police.mp3')
pygame.mixer.music.play()
input('Aperte algo para parar')
pygame.event.wait()
