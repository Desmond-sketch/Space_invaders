from pygame.image import load
from pygame.sprite import groupcollide
import alien


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
            
        
