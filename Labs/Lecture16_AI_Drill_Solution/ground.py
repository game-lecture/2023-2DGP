from pico2d import load_image

class Ground:
    def __init__(self):
        self.image = load_image('TUK_GROUND.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(1280 // 2, 1024 // 2)

