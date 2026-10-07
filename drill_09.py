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


def main():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    background = load_image('TUK_GROUND.png')
    character = load_image('animation_sheet.png')
    close_canvas()


if __name__ == '__main__':
    main()
