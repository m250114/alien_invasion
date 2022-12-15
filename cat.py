import pygame
import sys
import time

pygame.init()

screen = pygame.display.set_mode((1000,1000))
screen.fill((0,255,0))
screen_rect = screen.get_rect()


my_cat=pygame.image.load("images/cat.bmp")
my_cat_rect= my_cat.get_rect()
print(my_cat_rect)
blit(my_cat, screen.center)
screen.blit(my_cat, screen_rect.center)
pygame.display.flip()

time.sleep(5)