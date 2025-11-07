import pygame
import utils
import alien
import player
import sys

SCREEN_SIZE = [1_240, 7_20]
screen = pygame.display.set_mode(SCREEN_SIZE)
running = True
pygame.init()
pygame.display.set_caption("Space invaders")

ALL_FRAMES = utils.load_frames()
PLAYER = player.Player([ALL_FRAMES[7]], 200, 400)

Aliens = pygame.sprite.Group()
Players = pygame.sprite.Group()
Players.add(PLAYER)

spawned_aliens = utils.spawn_aliens(ALL_FRAMES, 5, 300, 40)
for i in spawned_aliens:
    Aliens.add(i)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0,0,0))
    Aliens.update()
    Players.update()
    Aliens.draw(screen)
    Players.draw(screen)
    
    
    
    pygame.display.flip()
