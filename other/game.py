import pygame
import sys
import time
# --- Constants
SCREEN_TITLE = "Platformer"

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
GROUND_MINUS = 20


class Ground:
    
    def __init__(self) -> None:
        self.x = 0
        self.tile_height = 128
        self.y = SCREEN_HEIGHT - self.tile_height
        self.width = SCREEN_WIDTH - self.x 
        self.height = self.tile_height
        self.image = pygame.image.load("assets/grass_block.png")
        self.surface = pygame.Surface((self.width, self.height))
        # Tile the image across the surface
        for x in range(0, self.width, self.image.get_width()):
            self.surface.blit(self.image, (x, 0))
            
    def draw(self, screen):
        # self.image.fill((0, 120, 0))

        screen.blit(self.surface, (self.x, self.y))

class Player:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        
        self.width = 40
        self.height = 40
        
        self.speed_x = 1
        self.speed_y = 2.5
        
        self.ismoving_left = True
        self.ismoving_right = True
    
        self.isjumping = False
        self.isgrounded = False
        self.image = pygame.image.load("assets/player64.png")
        self.can_jump = False
        self.jump_key_pressed = False
        self.max_jump_height = 600

    def update_pos(self):
        if self.ismoving_left:
            self.x += self.speed_x
        
        if self.ismoving_right:
            self.x -= self.speed_x
        
        self.jump()

    def jump(self):
        if self.can_jump and self.jump_key_pressed:
            self.y -= self.speed_y
            self.max_jump_height -= self.speed_y
            self.isjumping = True
        
        if self.max_jump_height <= 0:
            self.can_jump = False
            self.jump_key_pressed = False
            self.max_jump_height = 600
            self.isjumping = False
        
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

class MainGame:
    
    def __init__(self) -> None:
        """Initialize the game."""
        
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        self.running = True
        pygame.display.set_caption(SCREEN_TITLE)
        self.gound = Ground()
        self.player = Player()
        self.gravity = 1
        self.background = pygame.image.load("assets/background.png")
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    def event_loop(self):
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                self.close()

            if event.type in [pygame.KEYDOWN, pygame.KEYUP]:
                self.handle_keys(event, event.key)
    
    def close(self):
        self.running = False
    
    def handle_keys(self, event, key):
        def KEY_UP(key):
            if key == pygame.K_ESCAPE:
                self.close()
            if key == pygame.K_LEFT:
                self.player.ismoving_left = True
            if key == pygame.K_RIGHT:
                self.player.ismoving_right = True
            
            if key == pygame.K_UP:
                self.player.jump_key_pressed = False

        def KEY_DOWN(key):
            if key == pygame.K_ESCAPE:
                self.close()
            
            if key == pygame.K_RIGHT:
                self.player.ismoving_right = False
            
            if key == pygame.K_LEFT:
                self.player.ismoving_left = False
                
            if key == pygame.K_UP:
                self.player.jump_key_pressed = True
       
        if event.type == pygame.KEYUP:
            KEY_UP(key)
        elif event.type == pygame.KEYDOWN:
            KEY_DOWN(key)

    def update(self):
        global SCREEN_WIDTH
        SCREEN_WIDTH = self.screen.get_width()
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))
        self.event_loop()
        self.gound.draw(self.screen)
        self.gravity_update()
        self.player.update_pos()
        self.player.draw(self.screen)
        self.gound.width = SCREEN_WIDTH - self.gound.x   
        print(self.player.jump_key_pressed)
        pygame.display.update()
    
    def gravity_update(self):
        # print(self.player.isgrounded)
        if self.player.isgrounded is False:
            self.player.y += self.gravity
        # Check if the player is on the ground and if so, reset the y position
        if self.player.y >= (self.gound.y * 1.2 - self.gound.tile_height) - self.player.height and not self.player.isjumping:
            self.player.y = (self.gound.y * 1.2 - self.gound.tile_height) - self.player.height
            self.player.isgrounded = True
            self.gravity = 1
        
        if self.player.isgrounded:
            self.player.can_jump = True
        
        # Check if the player is on the ground and if not set player.isgrounded to False
        if not self.is_collision(self.player.x, self.player.y, 0, self.gravity):
            self.player.isgrounded = False

        # Prevent player from glitching thru the ground
        # Time wasted = 8 hours (Temp chunkey fix)
        if self.player.y >= (self.gound.y - GROUND_MINUS) - self.player.height:
            self.player.y -= self.gravity

    def run(self):
        while self.running:
            self.update()

        self.close_raw()
    
    def is_collision(self, x, y, x_change, y_change):
        return (
            x + x_change > self.gound.x
            and x + x_change < self.gound.x + self.gound.width
            and y + y_change > self.gound.y
            and y + y_change < self.gound.y + self.gound.height)
    
    def is_on_ground(self):
        return self.is_collision(self.player.x, self.player.y, 0, 1)
    
    def close_raw(self):
        pygame.quit()
        sys.exit(0)

def main():
    pygame.init()
    pygame.display.init()
    game = MainGame()
    game.run()

if __name__ == "__main__":
    main()
