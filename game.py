import pygame
import random


WIDTH = 300
HEIGHT = 600
FPS = 8


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)


BLOCK_SIZE = 30
GRID_WIDTH = WIDTH // BLOCK_SIZE
GRID_HEIGHT = HEIGHT // BLOCK_SIZE


SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
]


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

# Сетка для отслеживания заполненных клеток
grid = [[BLACK for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]


class Figure:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shape = random.choice(SHAPES)
        self.color = random.choice([RED, GREEN, BLUE, YELLOW, PURPLE])

    def draw(self):
        for i, row in enumerate(self.shape):
            for j, val in enumerate(row):
                if val:
                    pygame.draw.rect(screen, self.color,
                                     ((self.x + j) * BLOCK_SIZE,
                                      (self.y + i) * BLOCK_SIZE,
                                      BLOCK_SIZE, BLOCK_SIZE))

    def collide(self):
        for i, row in enumerate(self.shape):
            for j, val in enumerate(row):
                if val:
                    if i + self.y >= GRID_HEIGHT or \
                       j + self.x < 0 or \
                       j + self.x >= GRID_WIDTH or \
                       grid[i + self.y][j + self.x] != BLACK:
                        return True
        return False

    def lock(self):
        for i, row in enumerate(self.shape):
            for j, val in enumerate(row):
                if val:
                    grid[i + self.y][j + self.x] = self.color

    def move_left(self):
        self.x -= 1
        if self.collide():
            self.x += 1

    def move_right(self):
        self.x += 1
        if self.collide():
            self.x -= 1

    def rotate(self):
        new_shape = [list(row) for row in zip(*self.shape[::-1])]
        old_shape = self.shape
        self.shape = new_shape
        if self.collide():
            self.shape = old_shape

def clear_lines():
    global grid
    new_grid = [row for row in grid if any(color == BLACK for color in row)]
    cleared_lines = GRID_HEIGHT - len(new_grid)
    new_grid = [[BLACK] * GRID_WIDTH for _ in range(cleared_lines)] + new_grid
    grid = new_grid

# Функция для проверки окончания игры
def check_game_over():
    return any(color != BLACK for color in grid[0])

# Инициализация текущей фигуры
current_figure = Figure(4, 0)

# Функция для перемещения фигуры вниз
def go_down():
    global current_figure
    current_figure.y += 1
    if current_figure.collide():
        current_figure.y -= 1
        current_figure.lock()
        clear_lines()
        if check_game_over():
            return True
        current_figure = Figure(4, 0)
    return False

# Основной цикл игры
running = True
game_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                current_figure.move_left()
            elif event.key == pygame.K_RIGHT:
                current_figure.move_right()
            elif event.key == pygame.K_UP:
                current_figure.rotate()
            elif event.key == pygame.K_DOWN:
                if go_down():
                    game_over = True

    if not game_over:
        
        clock.tick(FPS)

        # Перемещаем фигуру вниз
        if go_down():
            game_over = True

        # Отрисовка экрана и текущей фигуры
        screen.fill(BLACK)
        for i, row in enumerate(grid):
            for j, color in enumerate(row):
                if color != BLACK:
                    pygame.draw.rect(screen, color, (j * BLOCK_SIZE, i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        current_figure.draw()

    pygame.display.flip()

pygame.quit()