from pico2d import *


CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 1024
FRAME_WIDTH = 100
FRAME_HEIGHT = 100
FRAME_COUNT = 8


def main():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    background = load_image('TUK_GROUND.png')
    close_canvas()


if __name__ == '__main__':
    main()
