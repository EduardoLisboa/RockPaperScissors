import pygame

class Image:
    
    r_img = pygame.transform.scale(
        pygame.image.load("images/rock.png"), 
        (25, 25)
    )
    p_img = pygame.transform.scale(
        pygame.image.load("images/paper.png"),
        (25, 25)
    )
    s_img = pygame.transform.scale(
        pygame.image.load("images/scissor.png"), 
        (25, 25)
    )

    IMAGES = {
        'r': r_img,
        'p': p_img,
        's': s_img
    }
