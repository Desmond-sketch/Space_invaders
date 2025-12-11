import pygame
import utils
import alien
import player
import barricade
from bullet import Bullet
import sys

SCREEN_SIZE = [1_240, 7_20]
screen = pygame.display.set_mode(SCREEN_SIZE)
running = True
pygame.init()
pygame.display.set_caption("Space invaders")
Font_large = pygame.font.Font("assets/Fonts/PressStart2P-Regular.ttf", 64)
Font_small = pygame.font.Font("assets/Fonts/PressStart2P-Regular.ttf", 16)

ALL_FRAMES = utils.load_frames()
PLAYER = player.Player([ALL_FRAMES[7]], 620, 650)

Aliens = pygame.sprite.Group()
Alien_Bullets = pygame.sprite.Group()
Bullets = pygame.sprite.Group()
Players = pygame.sprite.Group()
Players.add(PLAYER)
LEFT = False
RIGHT = True
Game_Over = False
Direction = RIGHT
Points = 0
Lives = 3

spawned_aliens = utils.spawn_aliens(ALL_FRAMES, 5, 300, 80)
for i in spawned_aliens:
    Aliens.add(i)

Movement_timer =0
clock = pygame.time.Clock()
Alien_speed = 1
Rpm = 5
Gun_cool = 0
Barricades = barricade.make_word_from_font(
    "XC7 Systems",
    start_x=100,
    start_y=450,
    font_size=200,
    block_size=4,
    block_gap=1,
    letter_gap=10,
    colour=(0, 255, 0)
)
def respawn_aliens():
    global Alien_speed, Points
    spawn_c = {"rows":{0:"alien1",1:"alien2", 2:"alien2",3:"alien3",4:"alien3"}, "speed" : Alien_speed + 1}
    spawned_aliens = utils.spawn_aliens(ALL_FRAMES, 5, 300, 80, spawn_code = spawn_c)
    Alien_speed += 1
    for i in spawned_aliens:
        Aliens.add(i)
    Points += 100
    
def check_aliens_past_player(aliens, boundary):
    for alien in aliens:
        if alien.rect.y > boundary:
            return True
    return False

def reset():
    global Game_Over, Lives, Barricades, Aliens, Points, PLAYER, Players
    Lives = 3
    for alien in Aliens:
        alien.kill()
        del alien
    Aliens = pygame.sprite.Group()
    respawn_aliens()
    Points = 0
    Barricades = barricade.make_word_from_font(
        "XC7 Systems",
        start_x=100,
        start_y=450,
        font_size=200,
        block_size=4,
        block_gap=1,
        letter_gap=10,
        colour=(0, 255, 0)
    )
    Game_Over = False
    PLAYER = player.Player([ALL_FRAMES[7]], 620, 650)
    Players.add(PLAYER)

blink_timer = 10
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if len(Players) >0 and PLAYER.rect.y <= 600 and not Game_Over:
        if keys[pygame.K_LEFT]:
            PLAYER.rect.x += -4
        if keys[pygame.K_RIGHT]:
            PLAYER.rect.x += 4
        if keys[pygame.K_SPACE]:
            if  len(Bullets) == 0:
                bullet = Bullet(PLAYER.rect.x + 12, PLAYER.rect.y, -10,(0,200,0))
                Bullets.add(bullet)
                utils.play_sounds(0)
                Gun_cool = Rpm
        if Gun_cool > 0:
            Gun_cool -= 1
    if keys[pygame.K_RETURN] and Game_Over:
        reset()
        print("reset")
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
    Alien_Bullets.update()
    Points += utils.check_aliens_shot(Bullets,Aliens)
    if(utils.check_player_shot(Alien_Bullets,Players) and PLAYER.rect.y <= 600 and not Game_Over):
        Lives -=1
        utils.play_sounds(-1)
        if Lives > 0:
            PLAYER = player.Player([ALL_FRAMES[7]], 620, 650)
            Players.add(PLAYER)
        
    aliens_past = check_aliens_past_player(Aliens, 600)
    if Lives < 1:
        Game_Over = True
        utils.draw_text(screen, text = "GAME OVER", text_size = 1000, x = 500, y = 400)
    elif aliens_past:
        utils.draw_text(screen, text = "GAME OVER", text_size = 1000, x = 500, y = 400)
    #code to make the player move into position after being respawned
    if PLAYER.rect.y > 600:
        PLAYER.rect.y -= 1
        
        
        
        
    Aliens.draw(screen)
    Players.draw(screen)
    Bullets.draw(screen)
    Barricades.draw(screen)
    Alien_Bullets.draw(screen)
    alien_bullet = utils.When_aliens_shoot(Aliens)
    if alien_bullet != None:
        Alien_Bullets.add(alien_bullet)
    utils.draw_text(screen, text = (f"Score : {Points}"), x = 0, y = 10, text_size = 16)
    utils.draw_text(screen, text = (f"Lives : {Lives}"), x = 1000, y = 10, text_size = 16)
    utils.barricades_interaction(Alien_Bullets, Bullets, Barricades)

    if blink_timer > 0:
        blink_timer -= 1

    if blink_timer < 20 and Game_Over:
        utils.draw_text(screen, text = "Press Enter to restart", text_size = 18, x = 300, y = 350)
    if blink_timer == 0:
        blink_timer = 30
    #text_score = Font_small.render(f"Score: {Points}", True, (0,250,0))
    #rect_score = text_score.get_rect()
    #screen.blit(text_score,rect_score)
    #text_lives = Font_small.render(f"Lives: ", True, (0,250,0))
    #rect_lives = text_lives.get_rect(center = (1000, 10))
    #screen.blit(text_lives,rect_lives)
    
    pygame.display.flip()
    clock.tick(60)

