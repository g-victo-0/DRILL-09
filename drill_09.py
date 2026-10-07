from pico2d import *


CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 1024
FRAME_WIDTH = 100
FRAME_HEIGHT = 100
FRAME_COUNT = 8
MOVE_SPEED = 6

running = True
x = CANVAS_WIDTH // 2
y = CANVAS_HEIGHT // 2
facing = 'right'
left_pressed = False
right_pressed = False
up_pressed = False
down_pressed = False


def handle_events():
    global running, left_pressed, right_pressed, up_pressed, down_pressed

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
            elif event.key == SDLK_UP:
                up_pressed = True
            elif event.key == SDLK_DOWN:
                down_pressed = True
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                left_pressed = False
            elif event.key == SDLK_RIGHT:
                right_pressed = False
            elif event.key == SDLK_UP:
                up_pressed = False
            elif event.key == SDLK_DOWN:
                down_pressed = False


def update_character():
    global x, y, facing

    dx = int(right_pressed) - int(left_pressed)
    dy = int(up_pressed) - int(down_pressed)

    x += dx * MOVE_SPEED
    y += dy * MOVE_SPEED

    if dx < 0:
        facing = 'left'
    elif dx > 0:
        facing = 'right'

    half_width = FRAME_WIDTH // 2
    half_height = FRAME_HEIGHT // 2
    x = max(half_width, min(CANVAS_WIDTH - half_width, x))
    y = max(half_height, min(CANVAS_HEIGHT - half_height, y))


def main():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    background = load_image('TUK_GROUND.png')
    character = load_image('animation_sheet.png')
    close_canvas()


if __name__ == '__main__':
    main()
