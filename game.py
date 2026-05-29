import pygame
import sys

# Инициализация Pygame
pygame.init()
pygame.mixer.init()

# Настройки экрана
CELL_SIZE = 16
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dungeon of Death_Pre-Alpha")
'''
1 - стена
0 - пустота
'''
room_map = [
    [1, 3, 1, 3, 1, 1, 3, 1, 1, 1, 3, 3, 3],
    [3, 4, 0, 0, 0, 4, 3, 4, 4, 1, 0, 4, 3],
    [3, 4, 0, 0, 0, 4, 1, 4, 0, 3, 3, 4, 1],
    [3, 4, 4, 0, 0, 0, 2, 4, 0, 0, 2, 0, 1],
    [1, 4, 0, 0, 0, 4, 3, 0, 4, 3, 1, 0, 1],
    [1, 0, 0, 0, 4, 0, 3, 0, 4, 1, 0, 0, 2],
    [1, 3, 3, 1, 1, 1, 1, 3, 3, 3, 1, 3, 3],
]
room_smal = [
    [1, 1, 3, 3, 1, 1, 1, 1],
    [0, 0, 0, 0, 4, 0, 0, 2],
    [0, 4, 0, 0, 0, 0, 0, 3],
    [0, 4, 4, 0, 0, 0, 4, 1],
    [3, 0, 0, 0, 0, 4, 4, 2],
    [1, 0, 4, 0, 0, 4, 4, 1],
    [1, 1, 1, 3, 3, 3, 3, 1],
]
comnatca_room = [
    [1, 3, 3, 3, 1, 1, 3, 1, 1, 1],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [4, 0, 0, 4, 0, 0, 4, 4, 0, 3],
    [0, 0, 4, 4, 0, 0, 0, 4, 0, 3],
    [0, 0, 0, 4, 0, 0, 0, 0, 0, 1],
    [3, 3, 1, 1, 1, 1, 3, 3, 3, 1],
]
crainaya_room = [
    [3, 3, 1, 1, 1, 3, 3, 3, 1],
    [3, 0, 0, 0, 0, 0, 4, 0, 1],
    [2, 0, 4, 4, 0, 0, 0, 0, 3],
    [1, 0, 4, 0, 0, 0, 4, 4, 3],
    [1, 0, 0, 4, 0, 0, 4, 4, 1],
    [3, 3, 3, 1, 1, 1, 1, 3, 1],
]
spusk_vniz = [
    [0, 0, 0],
    [0, 5, 0],
    [0, 0, 0],
    [1, 1, 1],
]
corridor_odin = [
    [3, 1],
    [4, 2],
    [0, 3],
    [4, 3],
    [0, 1],
    [0, 0],
    [1, 2],
]
corridor_dlin = [
    [3, 3, 3, 1, 1, 1, 1, 1, 3, 1],
    [4, 0, 0, 4, 0, 0, 0, 0, 4, 2],
    [1, 1, 1, 3, 2, 3, 3, 1, 1, 3],
]
corridor_vniz = [
    [1, 4, 3],
    [3, 4, 1],
    [3, 0, 1],
    [1, 0, 3],
    [1, 0, 3],
    [1, 0, 2],
    [1, 4, 1],
    [3, 3, 1],
]
corridor_verh = [
    [1, 4, 3],
    [3, 4, 1],
    [3, 0, 3],
    [1, 0, 3],
    [1, 0, 1],
    [1, 4, 1],
    [3, 4, 3],
    [0, 0, 1],
    [1, 3, 1],
]

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Задаем смещение всех комнат (в пикселях)
OFFSET_X = 0
OFFSET_Y = 0

room_smal_offset_x = len(room_map[0]) * CELL_SIZE + 32
room_smal_offset_y = len(room_map) * CELL_SIZE

corridor_odin_x = len(room_map[0]) * CELL_SIZE
corridor_odin_y = len(room_map) * CELL_SIZE

corridor_dlin_x = len(room_map[0]) * CELL_SIZE + 160
corridor_dlin_y = len(room_map) * CELL_SIZE

corridor_vniz_x = len(room_map[0]) * CELL_SIZE
corridor_vniz_y = len(room_map) * CELL_SIZE + 112

comnatca_room_x = len(room_map[0]) * CELL_SIZE + 48
comnatca_room_y = len(room_map) * CELL_SIZE + 144

corridor_verh_x = len(room_map[0]) * CELL_SIZE + 208
corridor_verh_y = len(room_map) * CELL_SIZE + 48

crainaya_room_x = len(room_map[0]) * CELL_SIZE + 304
crainaya_room_y = len(room_map) * CELL_SIZE - 16

spusk_vniz_x = len(room_map[0]) * CELL_SIZE + 160
spusk_vniz_y = len(room_map) * CELL_SIZE + 48

#ОТРИСОВКА КОМНАТ
room = [
    (room_map, 0, 112),
    (room_smal, room_smal_offset_x, room_smal_offset_y),
    (corridor_odin, corridor_odin_x, corridor_odin_y),
    (corridor_dlin, corridor_dlin_x, corridor_dlin_y),
    (corridor_vniz, corridor_vniz_x, corridor_vniz_y),
    (comnatca_room, comnatca_room_x, comnatca_room_y),
    (corridor_verh, corridor_verh_x, corridor_verh_y),
    (crainaya_room, crainaya_room_x, crainaya_room_y),
    (spusk_vniz, spusk_vniz_x, spusk_vniz_y),
]

#ОТРИСОВКА МОНСТРОВ
monsters = [
    (300, 400),
    (400, 300),
]

'''
sprite = pygame.image.load(...): Загружает изображение спрайта.

'''
# Игрок
player_sprite = pygame.image.load('Dungeon_of_Death/New_Sprait/Hero/Tenevoi_mag_parad.png')

# Стены, пол и двери
obiekt_sprite = pygame.image.load('Dungeon_of_Death/New_Sprait/Stena_Dang/Stoun_Sten.png')
sprite_dver = pygame.image.load('Dungeon_of_Death/New_Sprait/Stena_Dang/Stoun_Sten_dver.png')
staraya_stena = pygame.image.load('Dungeon_of_Death/New_Sprait/Stena_Dang/Stoun_Sten_rasteniya.png')

sprite_fon = pygame.image.load('Dungeon_of_Death/New_Sprait/Pol_Dang/Pol_Level_1.png')
zamshelii_pol = pygame.image.load('Dungeon_of_Death/New_Sprait/Pol_Dang/Pol_Level_1_Zamshelii.png')
luk_new_level = pygame.image.load('Dungeon_of_Death/New_Sprait/Pol_Dang/luk-level.png')

# Декорации


# Монстры
slizen = pygame.image.load('Dungeon_of_Death/New_Sprait/Vragi/Slizen_stoit.png')

# Оружие


#Что-то
enemy = {
    "x": 10 * CELL_SIZE,
    "y": 10 * CELL_SIZE,
    "sprite": slizen,
    "vidimost": 4
}

#Музыка и эмбиент загрузка
ambient_song = pygame.mixer.music.load('Dungeon_of_Death/Ambient/ambient.mp3')

#воспроизведение
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

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
player_x, player_y = align_to_grid(1 * CELL_SIZE, 8 * CELL_SIZE, CELL_SIZE)
#sliz_x, sliz_y = align_to_grid(19 * CELL_SIZE, 10 * CELL_SIZE, CELL_SIZE)
enemy["x"], enemy["y"] = align_to_grid(19 * CELL_SIZE, 10 * CELL_SIZE, CELL_SIZE)

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
move_interval = 0  # Интервал в 500 миллисекунд (0,5 секунды)

# Игровой цикл
clock = pygame.time.Clock()
running = True

while running:

    walls_rect = []

    # Внутри цикла отрисовки:
    '''
    for row_index, row in enumerate(level_map): — мы проходим по всей матрице уровня.
    x = col_index * CELL_SIZE + OFFSET_X — здесь мы переводим абстрактный индекс из матрицы в реальные пиксели на экране.
    rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE) — создаем невидимый математический квадрат.
    Он хранит в себе позицию и размер клетки.
    if cell == 1: ... else: ... — это ядро движка. Программа смотрит на число в матрице.
    '''
    for room_map, OFFSET_X, OFFSET_Y in room:
        for row_index, row in enumerate(room_map):
            for col_index, cell in enumerate(row):
                # Вычисляем позицию один раз для этой клетки
                x = col_index * CELL_SIZE + OFFSET_X
                y = row_index * CELL_SIZE + OFFSET_Y
                rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)

                if cell == 1:
                # Если в матрице 1 — рисуем красный блок
                    screen.blit(obiekt_sprite, rect)
                    walls_rect.append(rect) #для столкновений
                elif cell == 2:
                    screen.blit(sprite_dver, rect)
                elif cell == 3:
                    screen.blit(staraya_stena, rect)
                    walls_rect.append(rect)
                elif cell == 4:
                    screen.blit(zamshelii_pol, rect)
                elif cell == 5:
                    screen.blit(luk_new_level, rect)
                    walls_rect.append(rect)
                else:
                # Если в матрице 0 — рисуем белый блок (пустоту)
                    screen.blit(sprite_fon, rect)

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

        old_x, old_y = enemy["x"], enemy["y"]

        enemy_cell_x = enemy["x"] // CELL_SIZE
        enemy_cell_y = enemy["y"] // CELL_SIZE
        player_cell_x = player_x // CELL_SIZE
        player_cell_y = player_y // CELL_SIZE
        distance = max(abs(enemy_cell_x - player_cell_x),
                       abs(enemy_cell_y - player_cell_y))
        
        moved = False
        if distance <= enemy["vidimost"]:
            #преследование
            if enemy["x"] < player_x:
                enemy["x"] += CELL_SIZE
                moved = True
            elif enemy["x"] > player_x:
                enemy["x"] -= CELL_SIZE
                moved = True

            if enemy["y"] < player_y:
                enemy["y"] += CELL_SIZE
                moved = True
            elif enemy["y"] > player_y:
                enemy["y"] -= CELL_SIZE
                moved = True
        else:
            #случайное движение
            import random
            r = random.randint(0, 3)
            if r == 0:
                enemy["x"] += CELL_SIZE
            elif r == 1:
                enemy["x"] -= CELL_SIZE
            elif r == 2:
                enemy["y"] += CELL_SIZE
            elif r == 3:
                enemy["y"] -= CELL_SIZE
            moved = True

        # Начало изменений для проверки столкновений
        should_move = True

        #Проверка стен
        if moved:
            enemy_rect = pygame.Rect(
                enemy["x"] - CELL_SIZE // 2,
                enemy["y"] - CELL_SIZE // 2,
                CELL_SIZE,
                CELL_SIZE
            )
            collision = False
            for wall in walls_rect:
                if enemy_rect.colliderect(wall.inflate(-2, -2)):
                    collision = True
                    break

            if collision:
                enemy["x"], enemy["y"] = old_x, old_y
            
            #Проверка столкновения с игроком
            # if abs(enemy["x"] - player_x) < CELL_SIZE and abs(enemy["y"] - player_y) < CELL_SIZE:
            #     player_hp -= 10

        # Проверяем, находится ли потенциальная позиция игрока на клетке с красным кубом
        '''
        if potential_player_x == static_object_x and potential_player_y == static_object_y::
        Проверяет, совпадают ли координаты игрока с координатами статичного объекта (в данном случае, красного куба).

        should_move = False: Если позиция игрока совпадает с позицией красного куба,
        переменная should_move устанавливается в False, что означает, что игрок не может перемещаться на эту клетку. 
        '''
        player_rect = pygame.Rect(
            potential_player_x - CELL_SIZE // 2,
            potential_player_y - CELL_SIZE // 2,
            CELL_SIZE,
            CELL_SIZE
            )
        should_move = True
        for wall in walls_rect:
            if player_rect.colliderect(wall.inflate(-2, -2)):
                should_move = False
                break

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
#    camera_x = player_x - WIDTH // 2 + player_size // 2
#    camera_y = player_y - HEIGHT // 2 + player_size // 2

    # Отрисовка
    #screen.blit(sprite_fon, (statik_pol_x, statik_pol_y))

    # Рисуем статичный объект (на позиции в карте, с учетом смещения камеры)
    '''
    screen.blit(...): Рисует изображение на экране по координатам,
    скорректированным с учетом смещения камеры (camera_x и camera_y).
    '''
    #screen.blit(obiekt_sprite, (static_object_x, static_object_y))


    # Отрисовка игрока
    '''
    screen.blit(...): Рисует игрока на экране.
    '''
    screen.blit(player_sprite, (player_x - CELL_SIZE // 2, player_y - CELL_SIZE // 2))

    #Отрисовка монстров
    screen.blit(enemy["sprite"], (enemy["x"] - CELL_SIZE // 2, enemy["y"] - CELL_SIZE // 2))

    # Рисуем сетку
    '''
    for x in range(...): Цикл для создания вертикальных линий.
    pygame.draw.line(...): Рисует вертикальные линии по координате x.
    for y in range(...): Цикл для создания горизонтальных линий.
    pygame.draw.line(...): Рисует горизонтальные линии по координате y. 
    CELL_SIZE определяет расстояние между линиями.
    '''
    for x in range(0, WIDTH + 1, CELL_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT + 1, CELL_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (WIDTH, y))

    # Ограничение движения камеры по границам карты
#    map_width = 10000
#    map_height = 10000

#    camera_x = max(0, min(camera_x, map_width - WIDTH))
#    camera_y = max(0, min(camera_y, map_height - HEIGHT))

    # Обновление экрана
    pygame.display.update()
    screen.fill(BLACK)
    
    # Контроль FPS
    clock.tick(60)

# Завершение игры
pygame.quit()
sys.exit()