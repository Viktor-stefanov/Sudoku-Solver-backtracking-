import pygame
import sys
from solver import solve, is_valid
from board_generator import generate_board

pygame.init()

BLACK = (0, 0, 0)
HOVERED = (55, 89, 46)
WHITE = (255, 255, 255)
PICKED = (135, 175, 214)
GREEN = (20, 240, 20)
RED = (240, 20, 20)

S_WIDTH, S_HEIGHT = 900, 900
H_PAD = 50

C_WIDTH = (S_WIDTH - 5) / 9
C_HEIGHT = (S_HEIGHT - 5 - H_PAD) / 9

WIN = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
pygame.display.set_caption('Sodoku solver')

CLOCK = pygame.time.Clock()

font_size = int(C_WIDTH / 3)
big_font = pygame.font.SysFont('comicsansms', 70)
med_font = pygame.font.SysFont('comicsansms', 40)
small_font = pygame.font.SysFont('comicsansms', font_size)

def menu(win):
    if intro is True:
        main_text = big_font.render('SUDOKU game & solver', True, HOVERED)
        main_text_shadow = big_font.render('SUDOKU game & solver', True, BLACK)
        name_text = small_font.render('by Viktor Stefanov', True, BLACK)
        win.blit(main_text, (S_WIDTH // 15, 75))
        win.blit(main_text_shadow, (S_WIDTH // 15 - 3, 75))
        win.blit(name_text, (S_WIDTH // 1.71, 175))
        win.blit(name_text, (S_WIDTH // 1.71 - 1, 176))

        start_text = med_font.render('Pick a difficulty and press enter to begin:', True, BLACK)

        colors = [BLACK] * 4
        if hoverDiff is not None:
            colors[hoverDiff] = HOVERED
        if picked is not None:
            colors[picked] = GREEN

        easy = win.blit(small_font.render('EASY', True, colors[0]), (S_WIDTH // 5.5, 480))
        medium = win.blit(small_font.render('NORMAL', True, colors[1]), (S_WIDTH // 2.4, 480))
        hard = win.blit(small_font.render('HARD', True, colors[2]), (S_WIDTH // 1.4, 480))
        evil = win.blit(small_font.render('EVIL', True, colors[3]), (S_WIDTH // 1.29, 480))

        win.blit(start_text, (S_WIDTH // 15, 350))

        return (easy, medium, hard, evil)

def show_clock(win, start_time):
    seconds_passed  = (pygame.time.get_ticks() - start_time) // 1000
    if seconds_passed < 60:
        text = f'Time: {seconds_passed}'
    else:
        text = f'Time: {str(seconds_passed // 60)}:{str(seconds_passed % 60)}'
    seconds_text = small_font.render(text, True, 10)

    win.blit(seconds_text, (S_WIDTH // 1.3, S_HEIGHT - 50))

def update_numbers(win, bo, pos, clr, solved=False):
    for row in range(9):
        for col in range(9):
            num = str(bo[row][col])

            color = BLACK
            if (row, col) == pos:
                color = clr
            if solved is True:
                color = BLACK

            text = small_font.render(num, False, color)
            win.blit(text, (row * C_WIDTH + font_size // 0.8, col * C_HEIGHT + font_size // 1.5))

def draw_grid(win):
    for row in range(10):
        width = 2
        # widen the width of every 3rd row, so the squares will be well defined
        if row in (0, 3, 6, 9):
            width = 5
        pygame.draw.line(win, BLACK, (0, (2 + row * C_HEIGHT)), (S_WIDTH, 2 + row * C_HEIGHT), width)

    for col in range(10):
        width = 2
        # widen the width of every 3rd column, so the squares will be well defined
        if col in (0, 3, 6, 9):
            width = 5
        pygame.draw.line(win, BLACK, (2 + col * C_WIDTH, 0), (2 + col * C_WIDTH, S_HEIGHT - H_PAD - 1), width)

def redraw_window(win, start_time):
    win.fill(BLACK)
    show_clock(win, start_time)
    draw_grid(win)
    pygame.display.update()

def game():
    # dictionary mapping instead of a long if elif statement for picking numbers
    key_number = {
    pygame.K_1: 1,
    pygame.K_2: 2,
    pygame.K_3: 3,
    pygame.K_4: 4,
    pygame.K_5: 5,
    pygame.K_6: 6,
    pygame.K_7: 7,
    pygame.K_8: 8,
    pygame.K_9: 9,
    }
    start_time = pygame.time.get_ticks()
    FPS = 30
    while True:
        redraw_window(WIN, start_time)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    pass

        CLOCK.tick(FPS)
        pygame.display.update()


if __name__ == '__main__':
    pass