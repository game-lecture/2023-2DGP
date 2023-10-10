# 이것은 각 상태들을 객체로 구현한 것임.

from pico2d import load_image



class Idle:

    @staticmethod
    def enter():
        print('Idle Enter')

    @staticmethod
    def exit():
        print('Idle Exit')

    @staticmethod
    def do():
        print('Idle Do')

    @staticmethod
    def draw():
        pass



class StateMachine:
    def __init__(self):
        self.cur_state = Idle

    def start(self):
        self.cur_state.enter()

    def update(self):
        self.cur_state.do()

    def draw(self):
        self.cur_state.draw()





class Boy:
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.action = 3
        self.image = load_image('animation_sheet.png')
        self.state_machine = StateMachine()
        self.state_machine.start()

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        pass

    def draw(self):
        self.state_machine.draw()
