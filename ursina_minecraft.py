# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 00:15:04 2023

@author: harsh
"""

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

#importing textures
grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture = load_texture('assets/dirt_block.png')
sky_texture = load_texture('assets/skybox.png')
arm_texture = load_texture('assets/arm_texture.png')

#importing audio
punch_sound = Audio('assets/punch_sound', loop = False, autoplay = False)

block_pick = 1

window.fps_counter.enabled = True
window.exit_button.visible = True

def update():
    global block_pick
    
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()
    
    if held_keys['1'] : block_pick = 1
    if held_keys['2'] : block_pick = 2
    if held_keys['3'] : block_pick = 3
    if held_keys['4'] : block_pick = 4

class Voxel(Button):
    def __init__(self, position = (0,0,0), texture = grass_texture):
        super().__init__(
            parent = scene,
            position = position,
            model = 'assets/block', #'cube'
            origin_y = 0.5,
            texture = texture, #'white_cube'
            color = color.color(0,0, random.uniform(0.9,1)), #color.white
            #highlight_color = color.lime,
            scale = 0.5 #in order to prevent overlapping of blocks
            )
        
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down' :
                punch_sound.play()
                if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
                if block_pick == 2: voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture)
                if block_pick == 3: voxel = Voxel(position = self.position + mouse.normal, texture = brick_texture)
                if block_pick == 4: voxel = Voxel(position = self.position + mouse.normal, texture = dirt_texture)
            
            if key == 'right mouse down':
                punch_sound.play()
                destroy(self)

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = sky_texture,
            scale = 150,
            double_sided = True
            )

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'assets/arm',
            texture = arm_texture,
            scale = 0.2,
            rotation = Vec3(150, -10, 0),
            postition = Vec2(0.4, -0.6)
            )
        
    def active(self):
        self.position = Vec2(0.3, -0.5)
        
    def passive(self):
        self.position =Vec2(0.4, -0.6)
        

#initiate game with a floor
for z in range(20):
    for x in range(20):
        voxel = Voxel(position = (x,0,z))

player = FirstPersonController()
sky = Sky() #initiate sky
hand = Hand()

app.run()