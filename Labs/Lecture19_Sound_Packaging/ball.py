import random

from pico2d import *
import game_world

import server

class Ball:
    image = None
    zombie_eat_sound = None
    boy_eat_sound = None

    def __init__(self, x = None, y = None):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = x if x else random.randint(100, server.background.w - 100)
        self.y = y if y else random.randint(100, server.background.h - 100)

        # fill here

    def draw(self):
        self.image.draw(self.x - server.background.window_left, self.y - server.background.window_bottom)

    def update(self):
        pass

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
        match group:
            case 'boy:ball':
                # fill here
                game_world.remove_object(self)
