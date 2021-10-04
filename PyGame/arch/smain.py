import pygame

pygame.init()

class Screen():
    def __init__(self , W:int, H:int) -> None:
        self.screen = pygame.display.set_mode((W, H))

    def set_win_title(self ,title:str) -> None:
        self.screen.set_caption(title)

    def update(self) -> None:
        self.screen.update()

    def fill(self, R:int, G:int, B:int) -> None:
        self.screen.fill([R, G, B])

class Player():
    def __init__(self, image_path, X, Y, X_change, Y_change) -> None:
        self.playerImg = pygame.image.load(image_path)
        self.playerX = X
        self.playerY = Y
        self.playerX_change = X_change
        self.playerY_change = Y_change
    
    def display(self, X, Y , screen):
        screen.blit(self.playerImg , (X, Y))

