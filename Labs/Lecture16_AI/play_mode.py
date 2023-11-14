import random

from pico2d import *
import game_framework

import game_world
from boy import Boy
from ball import Ball
from zombie import Zombie
from ground import Ground


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()

        else:
            boy.handle_event(event)


def init():
    global boy

    ground = Ground()
    game_world.add_object(ground, 0)

    boy = Boy()
    game_world.add_object(boy, 2)
    game_world.add_collision_pair('boy:ball', boy, None)

    zombie = Zombie(300, 300)
    game_world.add_object(zombie, 2)
    game_world.add_collision_pair('zombie:ball', zombie, None)

    balls = [Ball() for _ in range(30)]
    for ball in balls:
        game_world.add_object(ball, 1)
        game_world.add_collision_pair('boy:ball', None, ball)
        game_world.add_collision_pair('zombie:ball', None, ball)


def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    game_world.handle_collisions()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

