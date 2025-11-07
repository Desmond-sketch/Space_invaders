from pygame.sprite import Sprite
class Player(Sprite):
    def __init__(self, frames, x, y):
        super().__init__()
        self.image = frames[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.frames = frames
        self.frame_no = 0

    def update(self):
        self.image = self.frames[self.frame_no]
        

        
    
