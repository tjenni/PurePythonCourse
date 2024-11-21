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


# _________________________________
#                                 /
# Animation mit Spritesheets     (
# ________________________________\
#
# In Arcade können Animationen mit `arcade.AnimatedWalkingSprite` implementiert 
# werden. Diese Klasse erleichtert das Hinzufügen von Animationen für verschiedene 
# Zustände wie Laufen, Stehen oder Springen.
#
# Die Animation erfolgt durch Hinzufügen von Bildern aus einem Spritesheet 
# oder einer Liste von Einzelbildern.


import arcade


class PlayerCharacter(arcade.Sprite):
    
    def __init__(self):
        super().__init__()

        # Default to face-right
        self.character_face_direction = 0 # 0:right, 1:left

        # Used for flipping between image sequences
        self.scale = 0.5
        self.cur_texture = 0
        
        # --- Load Textures ---

        path = ":resources:images/animated_characters/female_adventurer/femaleAdventurer"
        
        self.all_textures = {}

        # Load textures for idle standing
        self.all_textures["idle"] = self._load_texture_pair(f"{path}_idle.png")
        
        # Load textures for walking
        self.walk_textures = []
        for i in range(8):
            self.all_textures[f"walk {i}"] = self._load_texture_pair(f"{path}_walk{i}.png")


        # Set the initial texture
        self.texture = self.all_textures["idle"][0]
        

        # Hit box will be set based on the first image used.
        self.hit_box = self.texture.hit_box_points
    
    
    def _load_texture_pair(self, path):
        pair = [None, None]
        
        pair[0] = arcade.load_texture(path)
        pair[1] = arcade.load_texture(path, flipped_horizontally=True)
        
        return pair
    
    
    def update_animation(self, delta_time):

        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.character_face_direction == 0:
            self.character_face_direction = 1
        elif self.change_x > 0 and self.character_face_direction == 1:
            self.character_face_direction = 0

        # Idle animation
        if self.change_x == 0:
            self.texture = self.all_textures["idle"][self.character_face_direction]
            return

        # Walking animation
        self.cur_texture += 1
        if self.cur_texture > 7:
            self.cur_texture = 0
        
        self.texture = self.all_textures[f"walk {self.cur_texture}"][self.character_face_direction]
    
        
        
        
        
        


class AnimatedPlayerDemo(arcade.Window):
    """
    Demonstriert eine animierte Spielfigur mit Bewegungen und Animationen.
    """

    def __init__(self):
        super().__init__(800, 600, "Player Animation Demo")
        arcade.set_background_color(arcade.color.LIGHT_SKY_BLUE)

        # Spielfigur
        self.player = None

        # Bodenliste
        self.wall_list = None

        # Physik-Engine
        self.physics_engine = None
        
        
    def setup(self):
        """
        Initialisiert das Spielfeld, die Spielfigur und die Animationen.
        """
        # Wände (Boden)
        self.wall_list = arcade.SpriteList()
        for x in range(0, 1600, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", scale=0.5)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)

        # Animierter Spieler
        #self.player = arcade.Sprite(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png", scale=0.5)
        
        self.player = PlayerCharacter()
        
        self.player.center_x = 100
        self.player.center_y = 100
        self.player.scale = 0.5

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
        """
        Bewegt die Spielfigur bei Tasteneingaben.
        """
        if key == arcade.key.RIGHT:
            self.player.change_x = 5
            self.player.texture_change_distance = 20  # Animationsgeschwindigkeit
        elif key == arcade.key.LEFT:
            self.player.change_x = -5
            self.player.texture_change_distance = 20
        elif key == arcade.key.UP and self.physics_engine.can_jump():
            self.player.change_y = 12

    def on_key_release(self, key, modifiers):
        """
        Stoppt die Bewegung der Spielfigur, wenn die Tasten losgelassen werden.
        """
        if key in (arcade.key.LEFT, arcade.key.RIGHT):
            self.player.change_x = 0


# Hauptprogramm
window = AnimatedPlayerDemo()
window.setup()
arcade.run()
    
    
    
