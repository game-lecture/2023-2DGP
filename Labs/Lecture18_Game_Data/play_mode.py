import random
import json
import tomllib
import os

from pico2d import *
import game_framework
import game_world

import menu_mode
import server
from boy import Boy
from zombie import Zombie

from background import FixedBackground as Background

import server


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(menu_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_s:
            game_world.save()
        else:
            server.boy.handle_event(event)


def init():
    pass



def finish():
    server.background = None
    server.boy = None
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
