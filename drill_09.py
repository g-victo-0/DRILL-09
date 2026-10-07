from pico2d import *


CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 1024
FRAME_WIDTH = 100
FRAME_HEIGHT = 100
FRAME_COUNT = 8

running = True
x = CANVAS_WIDTH // 2
y = CANVAS_HEIGHT // 2
left_pressed = False
right_pressed = False
up_pressed = False
down_pressed = False


def handle_events():
    global running, left_pressed, right_pressed

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                left_pressed = True
            elif event.key == SDLK_RIGHT:
                right_pressed = True


def main():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    background = load_image('TUK_GROUND.png')
    character = load_image('animation_sheet.png')
    close_canvas()


if __name__ == '__main__':
    main()
