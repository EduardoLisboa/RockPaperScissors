import os
import pygame

# Initialize the game
pygame.init()

# Set up the screen
WIN = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Rock Paper Scissors - Simulator")

# Set up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Scissor:
    WIN_CASES = {
        'Rock': 'Scissor',
        'Paper': 'Rock',
        'Scissor': 'Paper'
    }

    def __init__(self, name: str, image: pygame.Surface) -> None:
        self.name = name
        self.beats = self.WIN_CASES[name]
        self.image = image
    
    def draw(self, win: pygame.Surface) -> None:
        WIN.fill(BLACK)
        win.blit(self.image, (300, 20))

    def battle(self, other):
        if self.win(other):
            return f"{self.name} wins"

    def win(self, other):
        return True if other.name == self.beats else False


def load_image(image_path):
    image = pygame.image.load(os.path.join("images", image_path))
    return pygame.transform.scale(image, (25, 25))


def main():
    run = True
    clock = pygame.time.Clock()

    scissor_img = load_image("scissor.png")
    print(type(scissor_img))
    scissor = Scissor("Scissor", scissor_img)

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            scissor.draw(WIN)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
