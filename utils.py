import pygame
from pygame.image import load
from pygame.sprite import groupcollide
import alien
import random
from bullet import Bullet
pygame.mixer.init()

all_sounds_dirs = ["Sounds/alienshoot1.wav", "Sounds/alienshoot2.wav", "Sounds/alienshoot2.wav", "Sounds/alienshoot3.wav", "Sounds/alienshoot3.wav", "Sounds/playerLaser.wav"]
all_sounds = []
all_frames = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
assets_dir = "assets/"
def load_frames():
    frames = []
    for i in all_frames:
        frame = load(assets_dir + i +".png")
        frames.append(frame)
    return frames

def spawn_aliens(frames, no_of_rows, startx, starty, spawn_code = {"rows":{0:"alien1",1:"alien2", 2:"alien2",3:"alien3",4:"alien3"}, "speed":1}):
    x, y = startx, starty
    spawned = []
    for i in range(no_of_rows):
        for j in range (11):
            alien_ = None
            if spawn_code["rows"][i] == "alien1":
                alien_ = alien.Alien(frames[0:2], x, y)
            elif spawn_code["rows"][i] == "alien2":
                alien_ = alien.Alien(frames[2:4], x, y)
            elif spawn_code["rows"][i] == "alien3":
                alien_ = alien.Alien(frames[4:6], x, y)
            if alien_ != None:
                alien.anim_speed = spawn_code["speed"]
                spawned.append(alien_)
            x += 40
        x = startx
                
        y += 40

    return spawned



def move_aliens(direction,aliens,movement_timer,world_bounds=[60,1180], speed = 1):
    direct = check_direction(world_bounds,aliens,direction)
    for alien in aliens:
        if direct and movement_timer == 0:
            alien.rect.x += speed
          
        elif direct != True and movement_timer == 0:
            alien.rect.x -= speed
            
    return direct
def check_direction(bounds,aliens,direct):
    new_dir = direct
    for alien in aliens:
        if alien.rect.x <= bounds[0]:
            new_dir = not (direct)
            break
        elif alien.rect.x >= bounds[1]:
            new_dir = not direct
            break
    if new_dir !=  direct:
        for alien in aliens:
            alien.rect.y += 10
    return new_dir
def check_aliens_shot(bullets,aliens):
    hits = groupcollide(bullets,aliens,True, True)
    points = 0
    for col in hits:
        points+=1
    return points
def check_player_shot(bullets,players):
    hits = groupcollide(bullets,players,True, True)
    #points = 0
    for col in hits:
        return True
    return False
def draw_text(screen, text = "Hello world", text_size = 24, x = 0, y = 100, colour = (0, 250, 0)):
    font = pygame.font.Font("assets/Fonts/PressStart2P-Regular.ttf", 24)
    text_surface = font.render(text, True, colour)
    screen.blit(text_surface, (x, y))

def barricades_interaction(alien_bullets, player_bullets, barricades):
    hits = groupcollide(alien_bullets,barricades,True, True)
    hits = groupcollide(player_bullets,barricades,True, True)

def When_aliens_shoot(aliens, upper_range = 100):
    no_of_aliens = len(aliens)
    chosen_alien = random.randint(0, no_of_aliens)
    aliens_to_list = list(aliens)
    count = 0
    choice = random.randint(0, upper_range)
    if choice == 0:
        for i in range(no_of_aliens):
            if i == chosen_alien:
                bullet = Bullet(aliens_to_list[i].rect.x + 12, aliens_to_list[i].rect.y+12, 4,(255,0,0))
                play_sounds(1)
                return bullet
    return None         

def load_sounds():
    for i in all_sounds_dirs:
        sound = pygame.mixer.Sound(assets_dir + i)
        all_sounds.append(sound)
load_sounds()

def play_sounds(index):
    all_sounds[index].play()



