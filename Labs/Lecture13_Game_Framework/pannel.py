from pico2d import load_image

class Pannel:
    def __init__(self):
        self.image = load_image('item_select.png')

    def draw(self):
        self.image.draw(400, 300)

    def update(self):
        pass