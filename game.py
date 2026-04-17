import pygame
import sys

# Инициализация Pygame
pygame.init()

# Настройки экрана
CELL_SIZE = 16
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dungeon of Death")
'''
1 - стена
0 - пустота
'''
room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Задаем смещение всей комнаты (в пикселях)
OFFSET_X = 9
OFFSET_Y = 9

'''
player_sprite = pygame.image.load(...): Загружает изображение игрока.

'''
player_sprite = pygame.image.load('Dungeon of Death/New_Sprait/Hero/Tenevoi_mag_parad.png')
obiekt_sprite = pygame.image.load('Dungeon of Death/New_Sprait/Stena_Dang/Stoun_Sten.png')
sprite_fon = pygame.image.load('Dungeon of Death/New_Sprait/Pol_Dang/Pol_Level_1.png')

# Функция для выравнивания позиции к центру клетки
def align_to_grid(pos_x, pos_y, cell_size):

    grid_x = pos_x // cell_size
    grid_y = pos_y // cell_size
    center_x = grid_x * cell_size + cell_size // 2
    center_y = grid_y * cell_size + cell_size // 2
    return center_x, center_y

# Игрок
'''
 initial_player_screen_center_x вычисляет координату X центра экрана,
 деля общую ширину экрана (WIDTH) на 2.
 Это используется для размещения игрока в центр экрана по оси X.

 ТОже самое мы делаем для Y.
'''
player_size = CELL_SIZE
initial_player_screen_center_x = WIDTH // 2
initial_player_screen_center_y = HEIGHT // 2
player_x, player_y = align_to_grid(initial_player_screen_center_x, initial_player_screen_center_y, CELL_SIZE)

# Статичный объект (в заданной позиции в игровом мире)
static_object_world_x = 100
static_object_world_y = 100
static_object_x, static_object_y = align_to_grid(static_object_world_x, static_object_world_y, CELL_SIZE)
statik_pol_x, statik_pol_y = align_to_grid(static_object_world_x, static_object_world_y, CELL_SIZE)

# Камера
camera_x = 0
camera_y = 0

# Переменные управления движением
direction = None
move_timer = 0
move_interval = 500  # Интервал в 500 миллисекунд (0,5 секунды)

# Игровой цикл
clock = pygame.time.Clock()
running = True

while running:
    # Внутри цикла отрисовки:
    '''
    for row_index, row in enumerate(level_map): — мы проходим по всей матрице уровня.
    x = col_index * CELL_SIZE + OFFSET_X — здесь мы переводим абстрактный индекс из матрицы в реальные пиксели на экране.
    rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE) — создаем невидимый математический квадрат.
    Он хранит в себе позицию и размер клетки.
    if cell == 1: ... else: ... — это ядро движка. Программа смотрит на число в матрице.
    '''
    for row_index, row in enumerate(room_map):
        for col_index, cell in enumerate(row):
            # Вычисляем позицию один раз для этой клетки
            x = col_index * CELL_SIZE + OFFSET_X
            y = row_index * CELL_SIZE + OFFSET_Y
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)

            if cell == 1:
            # Если в матрице 1 — рисуем красный блок
                screen.blit(obiekt_sprite, (rect.x - camera_x, rect.y - camera_y))
            else:
            # Если в матрице 0 — рисуем белый блок (пустоту)
                screen.blit(sprite_fon, (rect.x - camera_x, rect.y - camera_y))

    # Обработка событий
    '''
    KEYDOWN — это событие, указывающее на то, что какая-то клавиша была нажата.
    K_DOWN — это константа, указывающая на конкретную клавишу "вниз".
    '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                direction = event.key

    # Проверка на таймер перемещения
    '''
    current_time = pygame.time.get_ticks(): Получает текущее время в миллисекундах с начала игры.

    if current_time - move_timer >= move_interval and direction is not None::
    Проверяет, прошло ли достаточно времени с последнего перемещения игрока и есть ли направление движения.
    '''
    current_time = pygame.time.get_ticks()
    if current_time - move_timer >= move_interval and direction is not None:
        # Вычисляем потенциальную новую позицию игрока
        '''
        potential_player_x и potential_player_y: Переменные для расчета новой позиции игрока.

        Условия if direction == pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_UP:
        Определяют изменение координат игрока в зависимости от нажатой клавиши.
        '''
        potential_player_x = player_x
        potential_player_y = player_y

        if direction == pygame.K_LEFT:
            potential_player_x -= CELL_SIZE
        if direction == pygame.K_RIGHT:
            potential_player_x += CELL_SIZE
        if direction == pygame.K_DOWN:
            potential_player_y += CELL_SIZE
        if direction == pygame.K_UP:
            potential_player_y -= CELL_SIZE

        # Начало изменений для проверки столкновений
        should_move = True

        # Проверяем, находится ли потенциальная позиция игрока на клетке с красным кубом
        '''
        if potential_player_x == static_object_x and potential_player_y == static_object_y::
        Проверяет, совпадают ли координаты игрока с координатами статичного объекта (в данном случае, красного куба).

        should_move = False: Если позиция игрока совпадает с позицией красного куба,
        переменная should_move устанавливается в False, что означает, что игрок не может перемещаться на эту клетку. 
        '''
        if potential_player_x == static_object_x and potential_player_y == static_object_y: should_move = False
        if potential_player_x == statik_pol_x and potential_player_y == statik_pol_y: should_move = True

        # Если движение разрешено, применяем выравнивание по сетке
        if should_move:
            player_x, player_y = align_to_grid(potential_player_x, potential_player_y, CELL_SIZE)

            # Запоминаем время последнего движения
            move_timer = current_time
            # Сбрасываем направление после перемещения
            direction = None
        else:
            # Если движение не разрешено, просто сбрасываем направление
            direction = None

        # Запоминаем время последнего движения
        move_timer = current_time

        # Сбрасываем направление после перемещения
        direction = None

    # Обновление смещения камеры
    camera_x = player_x - WIDTH // 2 + player_size // 2
    camera_y = player_y - HEIGHT // 2 + player_size // 2

    # Отрисовка
    #screen.blit(sprite_fon, (statik_pol_x - camera_x, statik_pol_y - camera_y))

    # Рисуем статичный объект (на позиции в карте, с учетом смещения камеры)
    '''
    screen.blit(...): Рисует изображение на экране по координатам,
    скорректированным с учетом смещения камеры (camera_x и camera_y).
    '''
    #screen.blit(obiekt_sprite, (static_object_x - camera_x, static_object_y - camera_y))


    # Отрисовка игрока
    '''
    screen.blit(...): Рисует игрока на экране с учетом смещения камеры.
    '''
    screen.blit(player_sprite, (player_x - camera_x, player_y - camera_y))

    # Рисуем сетку
    '''
    for x in range(...): Цикл для создания вертикальных линий.
    pygame.draw.line(...): Рисует вертикальные линии по координате x.
    for y in range(...): Цикл для создания горизонтальных линий.
    pygame.draw.line(...): Рисует горизонтальные линии по координате y. 
    CELL_SIZE определяет расстояние между линиями.
    '''
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, WHITE, (x + CELL_SIZE/2, 0), (x + CELL_SIZE/2, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, WHITE, (0, y + CELL_SIZE/2), (WIDTH, y + CELL_SIZE/2))

    # Ограничение движения камеры по границам карты
    map_width = 10000
    map_height = 10000

    camera_x = max(0, min(camera_x, map_width - WIDTH))
    camera_y = max(0, min(camera_y, map_height - HEIGHT))

    # Обновление экрана
    pygame.display.update()
    
    # Контроль FPS
    clock.tick(60)

# Завершение игры
pygame.quit()
sys.exit()


'''
1) Разобратся с проблемами отрисовки. Никак не разберусь, решаю одну проблему, появляется другая.
'''