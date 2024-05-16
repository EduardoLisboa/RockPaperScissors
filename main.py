from random import randint
import pygame
from image import Image

# Initialize the game
pygame.init()

# Set up constants
WIDTH, HEIGHT = 700, 700
ITEM_WIDTH, ITEM_HEIGHT = 25, 25
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

    def __init__(self, id: int, name: str, x: int, y: int) -> None:
        self.id = id
        self.name = name
        self.beats = self.WIN_CASES[name]
        self.image = Image.IMAGES[name]
        self.x = x
        self.y = y
        self.width = ITEM_WIDTH
        self.height = ITEM_HEIGHT
        self.rect = self.get_rect()
    
    def draw(self, win: pygame.Surface) -> None:
        win.blit(self.image, (self.x, self.y))

    def battle(self, others):
        for other in others:
            if self == other or self.name == other.name:
                continue
            if self.rect_overlap(other):
                other.change(self.name) if self.win(other) else self.change(other.name)

    def win(self, other):
        return True if self.beats == other.name else False
    
    def change(self, name):
        self.name = name
        self.beats = self.WIN_CASES[name]
        self.image = Image.IMAGES[name]

    def rect_overlap(self, other):
        return self.rect.colliderect(other.rect)
    
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
        
        self.rect = self.get_rect()
    
    def get_rect(self):
        rect = self.image.get_bounding_rect()
        rect[0] += self.x
        rect[1] += self.y
        return rect
    
    def __eq__(self, other):
        return self.id == other.id


def generate_items(qtd_items: int) -> list[Item]:
    items = {
        'r': [],
        'p': [],
        's': []
    }
    items_list = []
    for i, name in enumerate(['r', 'p', 's'], start=1):
        for j, _ in enumerate(range(qtd_items)):
            if name == 'r':
                x = randint(ITEM_WIDTH, WIDTH//2 - 2*ITEM_WIDTH)
                y = randint(HEIGHT//2, HEIGHT - 2*ITEM_HEIGHT)
            elif name == 'p':
                x = randint(WIDTH//4, 3*(WIDTH//4) - 2*ITEM_WIDTH)
                y = randint(0, HEIGHT//2 - 2*ITEM_HEIGHT)
            else:
                x = randint(WIDTH//2, WIDTH - 2*ITEM_WIDTH)
                y = randint(HEIGHT//2, HEIGHT - 2*ITEM_HEIGHT)
            
            id_idx = int(f'{i}{j}')
            items[name].append(Item(id_idx, name, x, y))
    
    items_list.extend(items['r'])
    items_list.extend(items['p'])
    items_list.extend(items['s'])
    
    return items_list


def play(items: list[Item], move=True) -> None:
    WIN.fill(BLACK)
    for item in items:
        if move: item.move()
        item.battle(items)
        item.draw(WIN)


def check_winner(items) -> None | str:
    counter = {
        'r': 0,
        'p': 0,
        's': 0
    }
    for item in items:
        counter[item.name] += 1
    
    if counter['r'] == 0 and counter['p'] == 0:
        return 's'
    elif counter['r'] == 0 and counter['s'] == 0:
        return 'p'
    elif counter['p'] == 0 and counter['s'] == 0:
        return 'r'
    else:
        return None
    

def handle_win(items):
    win_dict = {
        'r': 'Rock',
        'p': 'Paper',
        's': 'Scissors'
    }
    winner = check_winner(items)
    if winner:
        play(items, move=False)
        print(f'{win_dict[winner]} wins!')
        pygame.time.delay(3000)
        return False
    return True


def main():
    run = True
    clock = pygame.time.Clock()

    items = generate_items(50)

    while run:
        clock.tick(30)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                run = False

        play(items)

        run = handle_win(items)

        pygame.display.update()

    
    pygame.quit()


if __name__ == "__main__":
    main()
