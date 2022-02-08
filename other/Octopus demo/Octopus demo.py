"""
Octopus demo in sea  by lixingqiu
python街机模块arcade制作的模拟海底动画章鱼哥

"""

__author__ = "lixingqiu"
__date__ = "2014/4/3"
__url__ = "http://www.lixingqiu.com/?p=313"
__qq__ = "406273900"

import os
import arcade
import random

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 685
SCREEN_TITLE = "Octopus demo python街机模块arcade制作的模拟海底动画章鱼哥 "

COIN_SCALE = 1.0
COIN_COUNT = 50

MOVEMENT_SPEED = 5

class Actor(arcade.AnimatedTimeSprite):
    def __init__(self,images,scale):
        super().__init__()
        while images:self.textures.append(arcade.load_texture(images.pop(0),scale= scale))

class Octopus(arcade.Sprite):
    def __init__(self,images):
        super().__init__()
        self.costume_amount = len(images)
        self.n = self.costume_amount                  # 只是为了缩短代码而设
        while images:self.textures.append(arcade.load_texture(images.pop(0)))
        self.costume_counter =  0
        self.costume_index = self.n - abs(self.costume_counter%(self.n*2) - self.n)
        self.set_texture(self.costume_index)
        self.frame_counter = 0
        
    def alt_costume(self):
        self.frame_counter += 1
        if self.frame_counter % 10 == 0 :
            self.set_texture(self.costume_index)
            self.costume_counter += 2                     # if raise GLException,turn 2 into a larger number      
            self.costume_index = self.n - abs(self.costume_counter%(self.n*2) - self.n) # 指向下一个造型         
            
        
class MyGame(arcade.Window): 

    def __init__(self, width, height, title):
        """ 初始化方法      """
        super().__init__(width, height, title)

        self.background = None
        self.octopus = None
        # 定义所有角色列表                    
        self.all_actor_list = None 
 
    def setup(self):
        self.all_actor_list = arcade.SpriteList() 

        bgimages = ["images/bg2" + os.sep  + f"{index:04d}"  + ".png" for index in range(1,16)]
        self.background = Actor(bgimages,1.0)
        self.background.center_x = SCREEN_WIDTH//2
        self.background.center_y = SCREEN_HEIGHT//2
        self.all_actor_list.append(self.background)

        octopus_images = ["images/octopus/" +  str(i) + ".png" for i in range(1,82)]
        self.octopus = Octopus(octopus_images)
        
        self.octopus.center_x = SCREEN_WIDTH//2
        self.octopus.center_y = SCREEN_HEIGHT//2
        self.octopus.alpha =  80
        self.all_actor_list.append(self.octopus)

        grass_images = ["images/grass/costume" + str(index) +   ".png" for index in range(1,10)]
        
        self.grass =  Actor(grass_images,0.5)
        self.grass.alpha = 60 
        
        self.grass.center_x = 100
        self.grass.center_y = 110
        self.all_actor_list.append(self.grass)
           
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """   渲染屏幕       """
   
        arcade.start_render() 
        self.all_actor_list.draw()   

    def update(self, delta_time):
        """ 更新角色"""

        self.all_actor_list.update()
        self.all_actor_list.update_animation()
        self.octopus.alt_costume()
 

def main():
    """ 主要方法 """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
