from pygame.image import load
import alien


all_frames = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
assets_dir = "assets/"
def load_frames():
    frames = []
    for i in all_frames:
        frame = load(assets_dir + i +".png")
        frames.append(frame)
    return frames

def spawn_aliens(frames, no_of_rows, startx, starty):
    spawn_code = {"rows":{0:"alien1",1:"alien2", 2:"alien2",3:"alien3",4:"alien3"}, "speed":0.05}
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
                spawned.append(alien_)
            x += 40
        x = startx
                
        y += 40

    return spawned
                
            
        
