import random
import server

from pico2d import *


class FixedBackground:

    def __init__(self):
        self.image = load_image('TUK_GROUND_FULL.png')
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

    def __getstate__(self):
        state = dict()
        return state

    def __setstate__(self, state):
        self.__init__()


    def draw(self):
        self.image.clip_draw_to_origin(self.window_left, self.window_bottom, self.cw, self.ch, 0, 0)

    def update(self):
        self.window_left = clamp(0, int(server.boy.x) - self.cw // 2, self.w - self.cw - 1)
        self.window_bottom = clamp(0, int(server.boy.y) - self.ch // 2, self.h - self.ch - 1)

    def handle_event(self, event):
        pass

