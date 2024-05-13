from random import randint
import pygame
from image import Image

# Initialize the game
pygame.init()

# Set up constants
WIDTH, HEIGHT = 600, 600
ITEM_WIDTH, ITEM_HEIGHT = 20, 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# Set up the screen
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors - Simulator")


class Item:
    WIN_CASES = {
        'r': 's',
        'p': 'r',
        's': 'p'
    }

    def __init__(self, name: str, x: int, y: int) -> None:
        self.name = name
        self.beats = self.WIN_CASES[name]
        self.image = Image.IMAGES[name]
        self.x = x
        self.y = y
        self.width = ITEM_WIDTH
        self.height = ITEM_HEIGHT
    
    def draw(self, win: pygame.Surface) -> None:
        win.blit(self.image, (self.x - self.width//2, self.y - self.height//2))

    def battle(self, other):
        if self.win(other):
            return f"{self.name} wins"

    def win(self, other):
        return True if other.name == self.beats else False
    
    def __eq__(self, other):
        return self.name == other.name


def generate_items(qtd_items: int) -> list[Item]:
    items = {
        'r': [],
        'p': [],
        's': []
    }
    items_list = []
    for name in ['r', 'p', 's']:
        for _ in range(qtd_items):
            if name == 'r':
                x = randint(25, WIDTH//3 - ITEM_WIDTH)
                y = randint(2*(HEIGHT//3), HEIGHT - ITEM_HEIGHT)
            elif name == 'p':
                x = randint(WIDTH//3, 2*(WIDTH//3) - ITEM_WIDTH)
                y = randint(0, HEIGHT//3 - ITEM_HEIGHT)
            else:
                x = randint(2*(WIDTH//3), WIDTH - ITEM_WIDTH)
                y = randint(2*(HEIGHT//3), HEIGHT - ITEM_HEIGHT)
            
            items[name].append(Item(name, x, y))
    
    items_list.extend(items['r'])
    items_list.extend(items['p'])
    items_list.extend(items['s'])
    
    return items_list


def main():
    run = True
    clock = pygame.time.Clock()


    items = generate_items(15)

    WIN.fill(BLACK)

    while run:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            for item in items:
                item.draw(WIN)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
