import time
import arcade
from player import Player
from ground import Ground , Box
from enemy import Enemy
from live import Lives



class Game(arcade.Window):
    def __init__(self):
        self.w = 1000
        self.h = 700
        self.gravity = 0.2
        self.win_check = 0
        self.me = Player()
        super().__init__(self.w , self.h ,"platformer game")
        self.background_image = arcade.load_texture("background.png")

        self.key = arcade.Sprite(":resources:images/items/keyYellow.png")
        self.key.center_x = 100
        self.key.center_y = 600
        self.key.width = 50
        self.key.height = 50

        self.lock = arcade.Sprite(":resources:images/tiles/lockYellow.png")
        self.lock.center_x = 900
        self.lock.center_y = 125
        self.lock.width = 50
        self.lock.height = 50

        self.x = 0
        self.live_list = []
        for i in range(self.me.count):
            self.live_list.append(Lives(880+self.x , 650))
            self.x +=30

        self.t1 = time.time()

        self.ground_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        

        for i in range(0, 1000 , 120):
            ground = Ground(i , 40)
            self.ground_list.append(ground)

        for i in range(400 , 800 , 120):
            box = Box(i , 250)
            self.ground_list.append(box)

        for i in range(100 , 300 , 120):
            box = Box(i ,500)
            self.ground_list.append(box)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.me, self.ground_list, gravity_constant = self.gravity)
        
        self.enemy_physics_engine_list = []



    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0 ,0 , self.w , self.h , self.background_image)

        if len(self.live_list) != 0:
            self.me.draw()
        
        for enemy in self.enemy_list:
            enemy.draw()

        for ground in self.ground_list:
            ground.draw()

        for i in range(len(self.live_list)):
            self.live_list[i].draw()

        try:
            self.key.draw()
        except:
            pass

        self.lock.draw()
        if self.win_check == 1:
            arcade.draw_text("You Won!" , self.width // 2 - 100 ,self.height // 2, arcade.color.RED, bold=True, font_size=40)
            arcade.finish_render()
            time.sleep(0.5)

        if len(self.live_list) == 0:
            arcade.draw_text("Game Over!" , self.width // 2 - 160 ,self.height // 2, arcade.color.RED, bold=True, font_size=40)
            arcade.finish_render()
            time.sleep(0.5)



    def on_update(self, delta_time):
        self.t2 = time.time()
        try:
            if arcade.check_for_collision(self.me , self.key):
                self.me.pocket.append(self.key)
                del self.key
        except:
            pass

        if arcade.check_for_collision(self.me , self.lock) and len(self.me.pocket) == 1:
            self.lock.texture = arcade.load_texture(":resources:images/items/flagGreen2.png")
            self.win_check = 1
            self.enemy_list.clear()

        
        if self.t2 - self.t1 > 3:
            new_enemy = Enemy()
            self.enemy_list.append(new_enemy)
            self.enemy_physics_engine_list.append(arcade.PhysicsEnginePlatformer(new_enemy, self.ground_list, gravity_constant= self.gravity))
            self.t1 = time.time()

        for item in self.enemy_physics_engine_list:
            item.update()

        for enemy in self.enemy_list:
            enemy.update_animation()
        
        for i in self.enemy_list:
            if arcade.check_for_collision(i, self.me):
                self.enemy_list.remove(i)
                self.live_list.pop(-1)

        if len(self.live_list) == 0:
            self.enemy_list.clear()    
            
        self.physics_engine.update()
        self.me.update_animation()



    def on_key_press(self, symbol, modifiers):
        match symbol:
            case arcade.key.LEFT:
                self.me.change_x = -1 * self.me.speed
            case arcade.key.RIGHT:
                self.me.change_x = +1 *self.me.speed
            case arcade.key.UP:
                if self.physics_engine.can_jump():
                    self.me.change_y = 10


    def on_key_release(self, symbol, modifiers):
        self.me.change_x = 0


game = Game()
arcade.run()
