import pygame
# ------------------------------
# Block Sprite
# ------------------------------

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, colour=(0,255,0), width=10, height=10):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(colour)
        self.rect = self.image.get_rect(topleft=(x, y))


# ----------------------------------------
# Convert ANY letter into a mask-based block pattern
# ----------------------------------------

def make_letter_from_font(letter, start_x, start_y,
                          font, block_size=8, block_gap=1,
                          colour=(0,255,0)):

    # render letter to a surface
    surf = font.render(letter, True, (255,255,255))
    mask = pygame.mask.from_surface(surf)

    blocks = pygame.sprite.Group()

    # loop through mask pixels
    for y in range(0, mask.get_size()[1], block_size + block_gap):
        for x in range(0, mask.get_size()[0], block_size + block_gap):

            # Check if ANY pixel in this block chunk is solid
            solid = False
            for dy in range(block_size):
                for dx in range(block_size):
                    if x+dx < mask.get_size()[0] and y+dy < mask.get_size()[1]:
                        if mask.get_at((x+dx, y+dy)) == 1:
                            solid = True
                            break
                if solid:
                    break

            if solid:
                block = Block(
                    start_x + x,
                    start_y + y,
                    colour,
                    block_size,
                    block_size
                )
                blocks.add(block)

    # width consumption for layout
    letter_width = surf.get_width() + block_size

    return blocks, letter_width


# ----------------------------------------
# Make a word from blocks using real font text
# ----------------------------------------

def make_word_from_font(word, start_x, start_y,
                        font_name=None, font_size=48,
                        block_size=6, block_gap=1,
                        letter_gap=20,
                        colour=(0,255,0)):

    # load font (default pygame font if None)
    font = pygame.font.Font(font_name, font_size)

    all_blocks = pygame.sprite.Group()
    x = start_x

    for letter in word:
        letter_blocks, w = make_letter_from_font(
            letter,
            x,
            start_y,
            font,
            block_size=block_size,
            block_gap=block_gap,
            colour=colour
        )
        all_blocks.add(letter_blocks)
        x += w + letter_gap

    return all_blocks
