import pygame
import utils
import alien
import player
from bullet import Bullet
import sys

SCREEN_SIZE = [1_240, 7_20]
screen = pygame.display.set_mode(SCREEN_SIZE)
running = True
pygame.init()
pygame.display.set_caption("Space invaders")

ALL_FRAMES = utils.load_frames()
PLAYER = player.Player([ALL_FRAMES[7]], 300, 600)

Aliens = pygame.sprite.Group()
Alien_Bullets = pygame.sprite.Group()
Bullets = pygame.sprite.Group()
Players = pygame.sprite.Group()
Players.add(PLAYER)
LEFT = False
RIGHT = True
Direction = RIGHT
Points = 0

spawned_aliens = utils.spawn_aliens(ALL_FRAMES, 5, 300, 40)
for i in spawned_aliens:
    Aliens.add(i)

Movement_timer =0
clock = pygame.time.Clock()
Alien_speed = 1
Rpm = 5
Gun_cool = 0
def respawn_aliens():
    global Alien_speed
    spawn_c = {"rows":{0:"alien1",1:"alien2", 2:"alien2",3:"alien3",4:"alien3"}, "speed" : Alien_speed + 1}
    spawned_aliens = utils.spawn_aliens(ALL_FRAMES, 5, 300, 40, spawn_code = spawn_c)
    Alien_speed += 1
    for i in spawned_aliens:
        Aliens.add(i)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        PLAYER.rect.x += -4
    if keys[pygame.K_RIGHT]:
        PLAYER.rect.x += 4
    if keys[pygame.K_SPACE]:
        if  len(Bullets) == 0:
            bullet = Bullet(PLAYER.rect.x + 12, PLAYER.rect.y, -10,(0,200,0))
            Bullets.add(bullet)
            Gun_cool = Rpm
    if Gun_cool > 0:
        Gun_cool -= 1
    #if PLAYER.rect.x > SCREEN_SIZE[0]:
        #PLAYER.rect.x = 0
    #if PLAYER.rect.x < 0:
        #PLAYER.rect.x = SCREEN_SIZE[0]
    if PLAYER.rect.x > SCREEN_SIZE[0]-20:
        PLAYER.rect.x = SCREEN_SIZE[0]-20
    if PLAYER.rect.x < 0+20:
        PLAYER.rect.x = 0+20
    screen.fill((0,0,0))
    #print(len(Bullets))
    Aliens.update()
    Players.update()
    Direction = utils.move_aliens(Direction,Aliens,Movement_timer, speed = Alien_speed)
    if Movement_timer == 0:
        Movement_timer = 5
    if Movement_timer >0:
        Movement_timer -= 1
    if len(Aliens) == 0:
        respawn_aliens()
    Bullets.update()
    utils.check_aliens_shot(Bullets,Aliens)
    Aliens.draw(screen)
    Players.draw(screen)
    Bullets.draw(screen)
    pygame.display.flip()
    clock.tick(60)

