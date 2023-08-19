# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 19:18:03 2023

@author: harsh
"""

from ursina import *

class Test_cube(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            color = color.white,
            texture = 'white_cube',
            rotation = Vec3(45,45,45)
            )
        

class Test_button(Button):
    def __init__(self):
        super().__init__(
            parent = scene, #neccessary to declare a parent or else the buttom would be massive
            model = 'cube',
            texture = 'brick',
            color = color.blue,
            highlight_color = color.red,
            pressed_color = color.lime)
    
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                print('button pressed')

def update():
    if held_keys['a']:
        aatest_sq.x -= 4*time.dt

app = Ursina()

test_sq = Entity(model = 'quad', color = color.red, scale = (1,4), position = (5,4))

test_cube = Test_button()

app.run()