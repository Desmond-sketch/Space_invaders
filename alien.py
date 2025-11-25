from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self, frames, x, y):
        super().__init__()
        self.image = frames[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.frames = frames
        self.frame_no = 0
        self.anim_timer = 0
        self.anim_speed = 1
    def update(self):
        self.image = self.frames[self.frame_no]
        
        if self.anim_timer < 20:
            self.anim_timer += self.anim_speed
        if self.anim_timer >= 20:
            self.anim_timer = 0
            if self.frame_no < len(self.frames) -1:
                self.frame_no += 1
            else:
                self.frame_no = 0
