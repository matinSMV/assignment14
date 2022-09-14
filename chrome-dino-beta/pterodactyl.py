import random
import arcade
class Pterodactyl(arcade.AnimatedWalkingSprite):
    def __init__(self, width, height, speed):
        super().__init__()
        self.walk_left_textures = [arcade.load_texture('images/pterodactyl0.png'), arcade.load_texture('images/pterodactyl1.png')]
        self.center_x = width
        self.center_y = random.randint(220, 320)
        self.change_x = speed 
        self.change_y = 0
        self.scale = 0.6