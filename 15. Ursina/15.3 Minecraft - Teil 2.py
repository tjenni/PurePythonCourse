# Tutorial https://www.youtube.com/watch?v=DHSRaVeQxIk

from turtle import position, pu
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# Variables
grass_texture = load_texture("_assets/Textures/Grass_Block.png")
stone_texture = load_texture("_assets/Textures/Stone_Block.png")
brick_texture = load_texture("_assets/Textures/Brick_Block.png")
dirt_texture = load_texture("_assets/Textures/Dirt_Block.png")
wood_texture = load_texture("_assets/Textures/Wood_Block.png")
sky_texture = load_texture("_assets/Textures/Skybox.png")
arm_texture = load_texture("_assets/Textures/Arm_Texture.png")
punch_sound = Audio("_assets/SFX/Punch_Sound.wav", loop = False, autoplay = False)
window.exit_button.visible = False
block_pick = 1



# Updates every frame
def update():
    global block_pick

    if held_keys["left mouse"] or held_keys["right mouse"]:
        hand.active()
    else:
        hand.passive()

    if held_keys["1"]: block_pick = 1
    if held_keys["2"]: block_pick = 2
    if held_keys["3"]: block_pick = 3
    if held_keys["4"]: block_pick = 4
    if held_keys["5"]: block_pick = 5



# Voxel (block) properties
class Voxel(Button):
    def __init__(self, position = (0, 0, 0), texture = grass_texture):
        super().__init__(
            parent = scene,
            position = position,
            model = "_assets/Models/Block",
            origin_y = 0.5,
            texture = texture,
            color = color.color(0, 0, random.uniform(0.9, 1)),
            highlight_color = color.light_gray,
            scale = 0.5
        )
    
    # What happens to blocks on inputs
    def input(self,key):
        if self.hovered:
            if key == "left mouse down":
                punch_sound.play()
                if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
                if block_pick == 2: voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture)
                if block_pick == 3: voxel = Voxel(position = self.position + mouse.normal, texture = brick_texture)
                if block_pick == 4: voxel = Voxel(position = self.position + mouse.normal, texture = dirt_texture)
                if block_pick == 5: voxel = Voxel(position = self.position + mouse.normal, texture = wood_texture)

            
            if key == "right mouse down":
                punch_sound.play()
                destroy(self)

# Skybox
class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = "Sphere",
            texture = sky_texture,
            scale = 150,
            double_sided = True
        )

# Arm
class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent =camera.ui,
            model = "_assets/Models/Arm",
            texture = arm_texture,
            scale = 0.2,
            rotation = Vec3(150, -10, 0),
            position = Vec2(0.4, -0.6)
        )
    
    def active(self):
        self.position = Vec2(0.3, -0.5)

    def passive(self):
        self.position = Vec2(0.4, -0.6)

# Increase the numbers for more cubes. For exapmle: for z in range(20)
for z in range(20):
    for x in range(20):
        for y in range(-10,0):
            voxel = Voxel(position = (x, y, z))


player = FirstPersonController()
player.cursor.disable()

hand = Hand()
sky = Sky()




app.run()
