from pygame.sprite import Sprite
from pygame import Surface
class Bullet(Sprite):
    def __init__(self, x, y, velocity, colour):
        super().__init__()
        self.image = Surface((4,15))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x,y
        self.image.fill(colour)
        self.velocity = velocity
    def update(self):
        self.rect.y += self.velocity
        if self.rect.y > 1000:
            self.kill()
        elif self.rect.y < -10:
            self.kill()
