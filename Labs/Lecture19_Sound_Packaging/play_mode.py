import random
import json
import tomllib
import os

from pico2d import *
import game_framework
import game_world

import server
from boy import Boy
from ball import Ball
from zombie import Zombie

# fill here
from background import FixedBackground as Background
# from background import TileBackground as Background
# from background import InfiniteBackground as Background

import server


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            server.boy.handle_event(event)


def init():

    hide_cursor()

    server.background = Background()
    game_world.add_object(server.background, 0)

    server.boy = Boy()
    game_world.add_object(server.boy, 1)
    game_world.add_collision_pair('boy:ball', server.boy, None)

    for _ in range(20):
        zombie = Zombie()
        game_world.add_object(zombie)
        game_world.add_collision_pair('zombie:ball', zombie, None)

    for _ in range(200):
        ball = Ball()
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
