import arcade

class Lives(arcade.Sprite):
    def __init__(self , x , y):
        super().__init__("live.png")
        self.width = 30
        self.height = 30
        self.center_x = x
        self.center_y = y