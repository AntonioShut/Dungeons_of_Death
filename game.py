import pygame
import sys

# Инициализация Pygame
pygame.init()
pygame.mixer.init()

# Настройки экрана
CELL_SIZE = 16
WIDTH, HEIGHT = 800, 800
SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
fullscreen = False
pygame.display.set_caption("Dungeon of Death_Pre-Alpha")

game_surface = pygame.Surface((WIDTH, HEIGHT))

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

sliz_x, sliz_y = align_to_grid(19 * CELL_SIZE, 10 * CELL_SIZE, CELL_SIZE)
sliz1_x, sliz1_y = align_to_grid(18 * CELL_SIZE, 19 * CELL_SIZE, CELL_SIZE)
sliz2_x, sliz2_y = align_to_grid(35 * CELL_SIZE, 8 * CELL_SIZE, CELL_SIZE)

#Для монстров
enemy = [
    {"x": sliz_x, "y": sliz_y, "sprite": slizen, "vidimost": 4},
    {"x": sliz1_x, "y": sliz1_y, "sprite": slizen, "vidimost": 4},
    {"x": sliz2_x, "y": sliz2_y, "sprite": slizen, "vidimost": 4},
]

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
                    game_surface.blit(obiekt_sprite, rect)
                    walls_rect.append(rect) #для столкновений
                elif cell == 2:
                    game_surface.blit(sprite_dver, rect)
                elif cell == 3:
                    game_surface.blit(staraya_stena, rect)
                    walls_rect.append(rect)
                elif cell == 4:
                    game_surface.blit(zamshelii_pol, rect)
                elif cell == 5:
                    game_surface.blit(luk_new_level, rect)
                    walls_rect.append(rect)
                else:
                # Если в матрице 0 — рисуем белый блок (пустоту)
                    game_surface.blit(sprite_fon, rect)

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

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_F11:
            fullscreen = not fullscreen
            if fullscreen:
                screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
            else:
                screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
        if event.key == pygame.K_ESCAPE:
            if fullscreen:
                fullscreen = False
                screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
    

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
        old_player_x, old_player_y = player_x, player_y

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

        for one_enemy in enemy:
            old_x, old_y = one_enemy["x"], one_enemy["y"]

            enemy_cell_x = one_enemy["x"] // CELL_SIZE
            enemy_cell_y = one_enemy["y"] // CELL_SIZE
            player_cell_x = player_x // CELL_SIZE
            player_cell_y = player_y // CELL_SIZE
            distance = max(abs(enemy_cell_x - player_cell_x),
                            abs(enemy_cell_y - player_cell_y))
        
            moved = False
            if distance <= one_enemy["vidimost"]:
                #преследование
                if one_enemy["x"] < player_x:
                    one_enemy["x"] += CELL_SIZE
                    moved = True
                elif one_enemy["x"] > player_x:
                    one_enemy["x"] -= CELL_SIZE
                    moved = True

                if one_enemy["y"] < player_y:
                    one_enemy["y"] += CELL_SIZE
                    moved = True
                elif one_enemy["y"] > player_y:
                    one_enemy["y"] -= CELL_SIZE
                    moved = True
            else:
                #случайное движение
                import random
                r = random.randint(0, 3)
                if r == 0:
                    one_enemy["x"] += CELL_SIZE
                elif r == 1:
                    one_enemy["x"] -= CELL_SIZE
                elif r == 2:
                    one_enemy["y"] += CELL_SIZE
                elif r == 3:
                    one_enemy["y"] -= CELL_SIZE
                moved = True

            # Начало изменений для проверки столкновений
            should_move = True

            #Проверка стен
            if moved:
                enemy_rect = pygame.Rect(
                    one_enemy["x"] - CELL_SIZE // 2,
                    one_enemy["y"] - CELL_SIZE // 2,
                    CELL_SIZE,
                    CELL_SIZE
                )
                collision = False
                for wall in walls_rect:
                    if enemy_rect.colliderect(wall.inflate(-2, -2)):
                        collision = True
                        break

                if collision:
                    one_enemy["x"], one_enemy["y"] = old_x, old_y

                # Проверка столкновений с другими монстрами
                for other in enemy:
                    if other != one_enemy and other["x"] == one_enemy["x"] and other["y"] == one_enemy["y"]:
                        one_enemy["x"], one_enemy["y"] = old_x, old_y
                        break

                # Проверка столкновения с игроком (новая логика)
                next_x = one_enemy["x"]
                next_y = one_enemy["y"]

                # Определяем, куда монстр пытался пойти
                if one_enemy["x"] != old_x:
                    next_x = old_x + (1 if one_enemy["x"] > old_x else -1)
                if one_enemy["y"] != old_y:
                    next_y = old_y + (1 if one_enemy["y"] > old_y else -1)

                # Если в следующей клетке игрок - откатываем монстра обратно
                if next_x == player_x and next_y == player_y:
                    one_enemy["x"] = old_x
                    one_enemy["y"] = old_y
            
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
    game_surface.blit(player_sprite, (player_x - CELL_SIZE // 2, player_y - CELL_SIZE // 2))

    #Отрисовка монстров
    for one_enemy in enemy:
        game_surface.blit(one_enemy["sprite"], (one_enemy["x"] - CELL_SIZE // 2, one_enemy["y"] - CELL_SIZE // 2))

    # Рисуем сетку
    '''
    for x in range(...): Цикл для создания вертикальных линий.
    pygame.draw.line(...): Рисует вертикальные линии по координате x.
    for y in range(...): Цикл для создания горизонтальных линий.
    pygame.draw.line(...): Рисует горизонтальные линии по координате y. 
    CELL_SIZE определяет расстояние между линиями.
    '''
    for x in range(0, WIDTH + 1, CELL_SIZE):
        pygame.draw.line(game_surface, WHITE, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT + 1, CELL_SIZE):
        pygame.draw.line(game_surface, WHITE, (0, y), (WIDTH, y))

    #Скреен
    #scaled_surface = pygame.transform.scale(game_surface, (SCREEN_WIDTH, SCREEN_HEIGHT), screen)
    scale = min(SCREEN_WIDTH / WIDTH, SCREEN_HEIGHT / HEIGHT)
    new_width = int(WIDTH * scale)
    new_height = int(HEIGHT * scale)
    scaled_surface = pygame.transform.scale(game_surface, (new_width, new_height))
    x_offset = (SCREEN_WIDTH - new_width) // 2
    y_offset = (SCREEN_HEIGHT - new_height) // 2

    # Ограничение движения камеры по границам карты
#    map_width = 10000
#    map_height = 10000

#    camera_x = max(0, min(camera_x, map_width - WIDTH))
#    camera_y = max(0, min(camera_y, map_height - HEIGHT))

    # ==========ИНВЕНТАРЬ==========
    inv_x = x_offset + new_width + 20
    inv_y = y_offset + 20
    inv_width = 280
    slot_size = 42
    slot_gap = 5

    # Экипировка
    equip_rect = pygame.Rect(inv_x, inv_y, inv_width, 210)
    pygame.draw.rect(screen, (40, 40, 50), equip_rect)
    pygame.draw.rect(screen, WHITE, equip_rect, 2)

    # Заголовок
    font_small = pygame.font.Font(None, 16)
    title = font_small.render("ЭКИПИРОВКА", True, (200, 200, 150))
    screen.blit(title, (inv_x + 10, inv_y + 3))

    # Броня (5 слотов)
    armor_slots = [
        ("Шлем", 0),
        ("Нагрудник", 1),
        ("Поножи", 2),
        ("Ботинки", 3),
        ("Перчатки", 4)
    ]

    for i, (name, _) in enumerate(armor_slots):
        slot_x = inv_x + 10 + i * (slot_size + slot_gap)
        slot_y = inv_y + 25
        slot_rect = pygame.Rect(slot_x, slot_y, slot_size, slot_size)
        pygame.draw.rect(screen, (60, 60, 70), slot_rect)
        pygame.draw.rect(screen, (150, 150, 150), slot_rect, 1)
        
        # Название под слотом
        name_text = font_small.render(name[:3], True, (180, 180, 180))
        screen.blit(name_text, (slot_x + 2, slot_y + slot_size + 2))

    # Оружие (5 слотов)
    weapon_slots = [
        ("Меч", 0),
        ("Посох", 1),
        ("Топор", 2),
        ("Лук", 3),
        ("Щит", 4)
    ]

    for i, (name, _) in enumerate(weapon_slots):
        slot_x = inv_x + 10 + i * (slot_size + slot_gap)
        slot_y = inv_y + 95
        slot_rect = pygame.Rect(slot_x, slot_y, slot_size, slot_size)
        pygame.draw.rect(screen, (60, 60, 70), slot_rect)
        pygame.draw.rect(screen, (150, 150, 150), slot_rect, 1)
        
        name_text = font_small.render(name[:3], True, (180, 180, 180))
        screen.blit(name_text, (slot_x + 2, slot_y + slot_size + 2))

    # Аксессуары (5 слотов)
    accessory_slots = [
        ("Амулет", 0),
        ("Кольцо", 1),
        ("Кольцо", 2),
        ("Кольцо", 3),
        ("Артеф", 4)
    ]

    for i, (name, _) in enumerate(accessory_slots):
        slot_x = inv_x + 10 + i * (slot_size + slot_gap)
        slot_y = inv_y + 165
        slot_rect = pygame.Rect(slot_x, slot_y, slot_size, slot_size)
        pygame.draw.rect(screen, (60, 60, 70), slot_rect)
        pygame.draw.rect(screen, (150, 150, 150), slot_rect, 1)
        
        name_text = font_small.render(name[:4], True, (180, 180, 180))
        screen.blit(name_text, (slot_x + 2, slot_y + slot_size + 2))

    # инвентарь
    inv_bottom_y = inv_y + 230
    inv_bottom_rect = pygame.Rect(inv_x, inv_bottom_y, inv_width, 250)
    pygame.draw.rect(screen, (35, 35, 45), inv_bottom_rect)
    pygame.draw.rect(screen, WHITE, inv_bottom_rect, 2)

    # Заголовок
    inv_title = font_small.render("ИНВЕНТАРЬ", True, (200, 200, 150))
    screen.blit(inv_title, (inv_x + 10, inv_bottom_y + 3))

    # Сетка инвентаря 5x4 (5 колонок, 4 строки = 20 слотов)
    inv_rows = 4
    inv_cols = 5

    for row in range(inv_rows):
        for col in range(inv_cols):
            slot_x = inv_x + 10 + col * (slot_size + slot_gap)
            slot_y = inv_bottom_y + 25 + row * (slot_size + slot_gap + 5)
            slot_rect = pygame.Rect(slot_x, slot_y, slot_size, slot_size)
            pygame.draw.rect(screen, (50, 50, 60), slot_rect)
            pygame.draw.rect(screen, (100, 100, 110), slot_rect, 1)
            
            # Пример пустых слотов (можно потом заполнить предметами)
            # empty_text = font_small.render("--", True, (80, 80, 80))
            # screen.blit(empty_text, (slot_x + 12, slot_y + 12))

        # кнопка для теста (опционально)
        # test_btn = pygame.Rect(inv_x + 50, inv_bottom_y + 175, 120, 20)
        # pygame.draw.rect(screen, (80, 60, 80), test_btn)
        # pygame.draw.rect(screen, (200, 150, 200), test_btn, 1)
        # test_text = font_small.render("Тест: добавить предмет", True, (200, 180, 200))
        # screen.blit(test_text, (test_btn.x + 5, test_btn.y + 3))

    # ====ИНТЕРФЕЙС ИГРОКА======
    panel_x = x_offset - 220  # левее игры на 220 пикселей
    panel_y = y_offset + 20
    panel_width = 200
    panel_height = SCREEN_HEIGHT - 40  # почти на весь экран

    # Фон панели
    pygame.draw.rect(screen, (30, 30, 40), (panel_x, panel_y, panel_width, panel_height))
    pygame.draw.rect(screen, WHITE, (panel_x, panel_y, panel_width, panel_height), 2)

    # Шрифты
    font_small = pygame.font.Font(None, 18)
    font_medium = pygame.font.Font(None, 22)
    font_large = pygame.font.Font(None, 28)

    y_offset_panel = panel_y + 10

    # 1. Спрайт лица (временный круг)
    face_rect = pygame.Rect(panel_x + 10, y_offset_panel, 60, 60)
    pygame.draw.circle(screen, (200, 180, 100), face_rect.center, 30)  # жёлтое лицо
    pygame.draw.circle(screen, WHITE, face_rect.center, 30, 2)
    # Глаза
    pygame.draw.circle(screen, (0, 0, 0), (face_rect.centerx - 10, face_rect.centery - 5), 4)
    pygame.draw.circle(screen, (0, 0, 0), (face_rect.centerx + 10, face_rect.centery - 5), 4)
    # Улыбка
    pygame.draw.arc(screen, (0, 0, 0), (face_rect.centerx - 10, face_rect.centery - 5, 20, 15), 0, 3.14, 2)

    # Имя рядом со спрайтом
    name_text = font_large.render("Никки", True, (255, 220, 150))
    screen.blit(name_text, (face_rect.right + 10, face_rect.y + 15))

    # Уровень
    lvl_text = font_medium.render("Уровень 1", True, (200, 200, 200))
    screen.blit(lvl_text, (face_rect.right + 10, face_rect.y + 40))

    y_offset_panel += 75

    # 2. Полоски здоровья и маны
    # Здоровье
    hp_percent = 100  # 100 из 100
    hp_width = int(170 * hp_percent / 100)
    pygame.draw.rect(screen, (60, 0, 0), (panel_x + 10, y_offset_panel, 170, 18))
    pygame.draw.rect(screen, (200, 0, 0), (panel_x + 10, y_offset_panel, hp_width, 18))
    pygame.draw.rect(screen, WHITE, (panel_x + 10, y_offset_panel, 170, 18), 1)
    hp_text = font_small.render("Здоровье 100/100", True, WHITE)
    screen.blit(hp_text, (panel_x + 15, y_offset_panel + 2))

    y_offset_panel += 22

    # Мана
    mp_percent = 100
    mp_width = int(170 * mp_percent / 100)
    pygame.draw.rect(screen, (0, 0, 60), (panel_x + 10, y_offset_panel, 170, 18))
    pygame.draw.rect(screen, (0, 100, 200), (panel_x + 10, y_offset_panel, mp_width, 18))
    pygame.draw.rect(screen, WHITE, (panel_x + 10, y_offset_panel, 170, 18), 1)
    mp_text = font_small.render("Мана 100/100", True, WHITE)
    screen.blit(mp_text, (panel_x + 15, y_offset_panel + 2))

    y_offset_panel += 30

    # 3. эффекты (2 пустых строчки)
    effect_title = font_small.render("Эффекты:", True, (150, 150, 200))
    screen.blit(effect_title, (panel_x + 10, y_offset_panel))
    y_offset_panel += 18
    effect1 = font_small.render("- Нет", True, (100, 100, 100))
    screen.blit(effect1, (panel_x + 10, y_offset_panel))
    y_offset_panel += 16
    effect2 = font_small.render("- Нет", True, (100, 100, 100))
    screen.blit(effect2, (panel_x + 10, y_offset_panel))

    y_offset_panel += 25

    # 4. характеристики (качаемые)
    stats_title = font_medium.render("Характеристики:", True, (200, 200, 100))
    screen.blit(stats_title, (panel_x + 10, y_offset_panel))
    y_offset_panel += 22

    stats = [
    ("Магия", 5),
    ("Сила", 3),
    ("Ловкость", 4),
    ("Тьма", 2)
    ]

    for stat_name, stat_value in stats:
        stat_text = font_small.render(f"{stat_name}: {stat_value}", True, (200, 200, 200))
        screen.blit(stat_text, (panel_x + 15, y_offset_panel))
        # Маленькая кнопка "+"
        plus_rect = pygame.Rect(panel_x + 160, y_offset_panel - 2, 18, 18)
        pygame.draw.rect(screen, (80, 80, 100), plus_rect)
        pygame.draw.rect(screen, WHITE, plus_rect, 1)
        plus_text = font_small.render("+", True, (200, 200, 100))
        screen.blit(plus_text, (plus_rect.x + 5, plus_rect.y - 1))
        y_offset_panel += 18

    y_offset_panel += 10

    # 5. магия (2 заклинания)
    spells_title = font_medium.render("Магия:", True, (150, 150, 200))
    screen.blit(spells_title, (panel_x + 10, y_offset_panel))
    y_offset_panel += 22

    spells = [
    ("Теневой удар", "15 маны"),
    ("Теневой щит", "20 маны")
    ]

    for spell_name, spell_cost in spells:
        spell_text = font_small.render(f"{spell_name} [{spell_cost}]", True, (180, 150, 220))
        screen.blit(spell_text, (panel_x + 15, y_offset_panel))
        y_offset_panel += 18

    y_offset_panel += 15

    # 6. LOG (журнал событий)
    log_title = font_medium.render("Журнал событий:", True, (200, 180, 100))
    screen.blit(log_title, (panel_x + 10, y_offset_panel))
    y_offset_panel += 22

    # Рамка для лога
    log_rect = pygame.Rect(panel_x + 10, y_offset_panel, 180, 60)
    pygame.draw.rect(screen, (20, 20, 30), log_rect)
    pygame.draw.rect(screen, (100, 100, 120), log_rect, 1)

    log_text = font_small.render("В разработке Log", True, (150, 150, 150))
    screen.blit(log_text, (log_rect.x + 10, log_rect.y + 22))

    # Обновление экрана
    pygame.display.update()

    game_surface.fill(BLACK)
    screen.blit(scaled_surface, (x_offset, y_offset))
    
    # Контроль FPS
    clock.tick(60)

# Завершение игры
pygame.quit()
sys.exit()