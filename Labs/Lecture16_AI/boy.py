# 이것은 각 상태들을 객체로 구현한 것임.

from pico2d import get_time, load_image, load_font, clamp, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT, SDLK_UP, SDLK_DOWN, \
    draw_rectangle

from ball import Ball
import game_world
import game_framework

# state event check
# ( state event type, event value )

def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT

def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT

def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT

def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT


def upkey_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_UP

def upkey_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_UP

def downkey_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_DOWN

def downkey_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_DOWN






def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE

def time_out(e):
    return e[0] == 'TIME_OUT'

# time_out = lambda e : e[0] == 'TIME_OUT'




# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Idle:

    @staticmethod
    def enter(boy, e):
        if boy.action == 0:
            boy.action = 2
        elif boy.action == 1:
            boy.action = 3

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(int(boy.frame) * 100, boy.action * 100, 100, 100, boy.x, boy.y)



class RunRight:
    @staticmethod
    def enter(boy, e):
        boy.action = 1
        pass

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        boy.x += RUN_SPEED_PPS * game_framework.frame_time
        boy.x = clamp(25, boy.x, 1280 - 25)
        boy.y = clamp(25, boy.y, 1024 - 25)
        pass

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(int(boy.frame) * 100, boy.action  * 100, 100, 100, boy.x, boy.y)


class RunRightUp:
    @staticmethod
    def enter(boy, e):
        boy.action = 1
        pass

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        boy.x += RUN_SPEED_PPS * game_framework.frame_time
        boy.y += RUN_SPEED_PPS * game_framework.frame_time
        boy.x = clamp(25, boy.x, 1280 - 25)
        boy.y = clamp(25, boy.y, 1024 - 25)
        pass

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(int(boy.frame) * 100, boy.action  * 100, 100, 100, boy.x, boy.y)

class RunRightDown:
    @staticmethod
    def enter(boy, e):
        boy.action = 1
        pass

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        boy.x += RUN_SPEED_PPS * game_framework.frame_time
        boy.y -= RUN_SPEED_PPS * game_framework.frame_time
        boy.x = clamp(25, boy.x, 1280 - 25)
        boy.y = clamp(25, boy.y, 1024 - 25)
        pass

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(int(boy.frame) * 100, boy.action  * 100, 100, 100, boy.x, boy.y)




class RunLeft:
    @staticmethod
    def enter(boy, e):
        boy.action = 0
        pass

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        boy.x -= RUN_SPEED_PPS * game_framework.frame_time
        boy.x = clamp(25, boy.x, 1280 - 25)
        boy.y = clamp(25, boy.y, 1024 - 25)

        pass

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(int(boy.frame) * 100, boy.action  * 100, 100, 100, boy.x, boy.y)


class RunLeftUp:
    @staticmethod
    def enter(boy, e):
        boy.action = 0
        pass

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        boy.x -= RUN_SPEED_PPS * game_framework.frame_time
        boy.y += RUN_SPEED_PPS * game_framework.frame_time
        boy.x = clamp(25, boy.x, 1280 - 25)
        boy.y = clamp(25, boy.y, 1024 - 25)

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(int(boy.frame) * 100, boy.action * 100, 100, 100, boy.x, boy.y)


class RunLeftDown:
    @staticmethod
    def enter(boy, e):
        boy.action = 0
        pass

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        boy.x -= RUN_SPEED_PPS * game_framework.frame_time
        boy.y -= RUN_SPEED_PPS * game_framework.frame_time
        boy.x = clamp(25, boy.x, 1280 - 25)
        boy.y = clamp(25, boy.y, 1024 - 25)

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(int(boy.frame) * 100, boy.action  * 100, 100, 100, boy.x, boy.y)




class RunUp:
    @staticmethod
    def enter(boy, e):
        if boy.action == 2:
            boy.action = 0
        elif boy.action == 3:
            boy.action = 1


    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        boy.y += RUN_SPEED_PPS * game_framework.frame_time
        boy.x = clamp(25, boy.x, 1280 - 25)
        boy.y = clamp(25, boy.y, 1024 - 25)
        pass

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(int(boy.frame) * 100, boy.action * 100, 100, 100, boy.x, boy.y)


class RunDown:
    @staticmethod
    def enter(boy, e):
        if boy.action == 2:
            boy.action = 0
        elif boy.action == 3:
            boy.action = 1
        pass

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        boy.y -= RUN_SPEED_PPS * game_framework.frame_time
        boy.x = clamp(25, boy.x, 1280 - 25)
        boy.y = clamp(25, boy.y, 1024 - 25)
        pass

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(int(boy.frame) * 100, boy.action * 100, 100, 100, boy.x, boy.y)


class StateMachine:
    def __init__(self, boy):
        self.boy = boy
        self.cur_state = Idle
        self.transitions = {
            Idle: {right_down: RunRight, left_down: RunLeft, left_up: RunRight, right_up: RunLeft, upkey_down: RunUp, downkey_down: RunDown, upkey_up: RunDown, downkey_up: RunUp},
            RunRight: {right_up: Idle, left_down: Idle, upkey_down: RunRightUp, upkey_up: RunRightDown, downkey_down: RunRightDown, downkey_up: RunRightUp},
            RunRightUp: {upkey_up: RunRight, right_up: RunUp, left_down: RunUp, downkey_down: RunRight},
            RunUp: {upkey_up: Idle, left_down: RunLeftUp, downkey_down: Idle, right_down: RunRightUp, left_up: RunRightUp, right_up: RunLeftUp},
            RunLeftUp: {right_down: RunUp, downkey_down: RunLeft, left_up: RunUp, upkey_up: RunLeft},
            RunLeft: {left_up: Idle, upkey_down: RunLeftUp, right_down: Idle, downkey_down: RunLeftDown, upkey_up: RunLeftDown, downkey_up: RunLeftUp},
            RunLeftDown: {left_up: RunDown, downkey_up: RunLeft, upkey_down: RunLeft, right_down: RunDown},
            RunDown: {downkey_up: Idle, left_down: RunLeftDown, upkey_down: Idle, right_down: RunRightDown, left_up: RunRightDown, right_up: RunLeftDown},
            RunRightDown: {right_up: RunDown, downkey_up: RunRight, left_down: RunDown, upkey_down: RunRight}
        }

    def start(self):
        self.cur_state.enter(self.boy, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.boy)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.boy, e)
                self.cur_state = next_state
                self.cur_state.enter(self.boy, e)
                return True

        return False

    def draw(self):
        self.cur_state.draw(self.boy)








class Boy:
    def __init__(self):
        self.x, self.y = 1280 // 2, 1024 // 2
        self.frame = 0
        self.action = 3
        self.image = load_image('animation_sheet.png')
        self.font = load_font('ENCR10B.TTF', 40)
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.ball_count = 0


    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
        self.font.draw(self.x-10, self.y + 60, f'{self.ball_count}', (0, 0, 255))
        draw_rectangle(*self.get_bb())

    # fill here
    def get_bb(self):
        return self.x - 20, self.y - 50, self.x + 20, self.y + 50

    # fill here
    def handle_collision(self, group, other):
        if group == 'boy:ball':
            self.ball_count += 1



