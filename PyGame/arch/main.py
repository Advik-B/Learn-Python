import pygame

pygame.init() # Initalise pygame

# Create the screen
screen = pygame.display.set_mode((1000 , 800))

# Title and screen
pygame.display.set_caption('Demo')
# icon = pygame.image.load(r'assets\heros\6.png')
# pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load(r'assets\images\target icon icon.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

def player(x, y):
    screen.blit(playerImg , (x , y))



# Game Loop
running = True
while running:
    # RGB: Red , Green, Blue
    screen.fill([0, 0, 0])    #[153 , 146 , 255]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -.25
            
            if event.key == pygame.K_RIGHT:
                playerX_change = .25

            if event.key == pygame.K_UP:
                playerY_change = -.25

            if event.key == pygame.K_DOWN:
                playerY_change = .25

            if event.key == pygame.K_ESCAPE:
                running = False
    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                playerX_change = 0
            if event.key == pygame.K_RIGHT:
                playerX_change = 0

            if event.key == pygame.K_UP:
                playerY_change = 0
            if event.key == pygame.K_DOWN :
                playerY_change = 0


    playerY += playerY_change
    playerX += playerX_change
    player(playerX , playerY)
    pygame.display.update()