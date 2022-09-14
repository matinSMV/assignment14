import random
import arcade
class Cactus(arcade.Sprite):
    def __init__(self, width, height, speed):
        super().__init__()
        self.pic_path = random.choice(['images/cactus1_night.png','images/test-cactus4_night.png'])
        self.texture = arcade.load_texture(self.pic_path)
        self.center_x = width
        self.center_y = 84
        self.change_x = speed 
        self.change_y = 0
        self.width = 90
        self.height = 90
        self.scale = 0.9