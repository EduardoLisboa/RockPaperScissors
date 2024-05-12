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
    def __init__(self, image):
        self.name = "Scissor"
        self.beats = "Paper"
        self.image = image
    
    def draw(self, win):
        win.blit(self.image, (300, 300))


def load_image(image_path):
    image = pygame.image.load(os.path.join("images", image_path))
    return pygame.transform.scale(image, (30, 30))


def main():
    run = True
    clock = pygame.time.Clock()

    scissor_img = load_image("scissor.png")
    scissor = Scissor(scissor_img)

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            scissor.draw(WIN)

        WIN.fill(BLACK)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
