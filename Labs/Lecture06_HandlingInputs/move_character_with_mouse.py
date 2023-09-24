from pico2d import *


# fill here


character = load_image('animation_sheet.png')


def handle_events():
    global running

    # fill here

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        # fill here


running = True
frame = 0

# fill here



while running:
    clear_canvas()

    # fill here

    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()




