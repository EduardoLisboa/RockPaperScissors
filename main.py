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
    
    def move(self):
        self.x += randint(-5, 5)
        self.y += randint(-5, 5)

        if self.x <= 0:
            self.x = 0
        elif self.x >= WIDTH - self.width:
            self.x = WIDTH - self.width
        
        if self.y <= 0:
            self.y = 0
        elif self.y >= HEIGHT - self.height:
            self.y = HEIGHT - self.height
    
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
                x = randint(ITEM_WIDTH, WIDTH//2 - 2*ITEM_WIDTH)
                y = randint(HEIGHT//2, HEIGHT - 2*ITEM_HEIGHT)
            elif name == 'p':
                x = randint(WIDTH//3, 2*(WIDTH//3) - 2*ITEM_WIDTH)
                y = randint(0, HEIGHT//2 - 2*ITEM_HEIGHT)
            else:
                x = randint(WIDTH//2, WIDTH - 2*ITEM_WIDTH)
                y = randint(HEIGHT//2, HEIGHT - 2*ITEM_HEIGHT)
            
            items[name].append(Item(name, x, y))
    
    items_list.extend(items['r'])
    items_list.extend(items['p'])
    items_list.extend(items['s'])
    
    return items_list


def play(items: list[Item]) -> None:
    WIN.fill(BLACK)
    for item in items:
        item.move()
        item.draw(WIN)


def main():
    run = True
    clock = pygame.time.Clock()


    items = generate_items(30)


    while run:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN and event.key == pygame.Q:
                run = False


        play(items)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
