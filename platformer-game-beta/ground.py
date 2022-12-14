import arcade

class Ground(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.texture = arcade.load_texture(":resources:images/tiles/grassMid.png")
        self.center_x = x
        self.center_y = y
        self.width = 125
        self.height = 125

class Box(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.texture = arcade.load_texture(":resources:images/tiles/grassHalf_mid.png")
        self.center_x = x
        self.center_y = y
        self.width = 120
        self.height = 120