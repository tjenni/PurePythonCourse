#              _______________________________
#       ______|                               |_____
#       \     |   12.11 SPIELER ANIMIEREN     |    /
#        )    |_______________________________|   (
#       /________)                        (________\     21.11.24 von T. Jenni, CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)


# Animierte Spielfiguren sind ein zentraler Bestandteil vieler Spiele. 
# Animationen machen Bewegungen realistischer und lebendiger, indem sie 
# verschiedene Bilder (Frames) anzeigen, während sich der Spieler bewegt.

# Dieses Kapitel zeigt dir, wie du eine animierte Spielfigur mit Arcade 
# erstellst. Wir werden lernen:
#
# - Wie du Animationen für eine Spielfigur einrichtest.
#
# - Wie Animationen auf Bewegungen wie Laufen oder Springen reagieren.
#
# - Wie man Standbilder verwendet, wenn sich der Spieler nicht bewegt.


import arcade


class PlayerCharacter(arcade.Sprite):
    
    def __init__(self):
        super().__init__()

        self.face_direction = 0 # 0:right, 1:left

        self.scale = 0.5

        self.cur_texture = 0
        
        # load textures 
        path = ":resources:images/animated_characters/female_adventurer/femaleAdventurer"

        self.all_textures = {}

        # Load textures for idle standing
        self.all_textures["idle"] = self._load_texture_pair(f"{path}_idle.png")
        
        # Load textures for walking
        for i in range(8):
            self.all_textures[f"walk {i}"] = self._load_texture_pair(f"{path}_walk{i}.png")

        # Set the initial texture
        self.texture = self.all_textures["idle"][0]
        
        # Hit box will be set based on the first image used.
        self.hit_box = self.texture.hit_box_points
    
    
    def _load_texture_pair(self, path):
        return  [
            arcade.load_texture(path),
            arcade.load_texture(path, flipped_horizontally=True)
        ]
    

    def update_animation(self, delta_time):

        # Figure out if we need to flip face left or right
        if self.change_x < 0:
            self.face_direction = 1

        elif self.change_x > 0:
            self.face_direction = 0

        # Idle animation
        if self.change_x == 0:
            self.texture = self.all_textures["idle"][self.face_direction]
            return

        # Walking animation
        self.cur_texture += 1
        if self.cur_texture > 7:
            self.cur_texture = 0
        
        self.texture = self.all_textures[f"walk {self.cur_texture}"][self.face_direction]
    
        
        
        
        
        


class AnimatedPlayerDemo(arcade.Window):
    """
    Demonstriert eine animierte Spielfigur mit Bewegungen und Animationen.
    """

    def __init__(self):
        super().__init__(800, 600, "Player Animation Demo")
        arcade.set_background_color(arcade.color.LIGHT_SKY_BLUE)

        self.player = None

        self.wall_list = None

        self.physics_engine = None
        
        
    def setup(self):
        
        # Wände (Boden)
        self.wall_list = arcade.SpriteList()
        for x in range(0, 1600, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", scale=0.5)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)

        # Animierter Spieler
        self.player = PlayerCharacter()
        
        self.player.center_x = 100
        self.player.center_y = 100

        # Physik-Engine einrichten
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player, gravity_constant=0.5, walls=self.wall_list)

    def on_draw(self):
        arcade.start_render()

        self.wall_list.draw()
        self.player.draw()


    def on_update(self, delta_time):
        self.physics_engine.update()
        self.player.update_animation(delta_time)
        

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.player.change_x = 5
            self.player.texture_change_distance = 20  # Animationsgeschwindigkeit
        elif key == arcade.key.LEFT:
            self.player.change_x = -5
            self.player.texture_change_distance = 20
        elif key == arcade.key.UP and self.physics_engine.can_jump():
            self.player.change_y = 12

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.LEFT, arcade.key.RIGHT):
            self.player.change_x = 0


# Hauptprogramm
window = AnimatedPlayerDemo()
window.setup()
arcade.run()
    
    
    
