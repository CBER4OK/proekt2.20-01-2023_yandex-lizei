import sqlite3
import sys
from turtledemo import clock

# Импортируем библиотеку pygame
import pygame
from pygame import *
from player import *
from blocks import *

FPS = 60
pygame.init()
pygame.display.set_caption('g')
size = width, height = 800, 800
display = pygame.display
screen = pygame.display.set_mode(size)
# Объявляем переменные
WIN_WIDTH = 800  # Ширина создаваемого окна
WIN_HEIGHT = 640  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#000000"


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def terminate():
    pygame.quit()
    sys.exit()


def show_message(screen, param, param1):
    pass


def start_screen():
    con = sqlite3.connect("qwe.db")
    cur = con.cursor()
    # Получили результат запроса, который ввели в текстовое поле
    result = cur.execute("SELECT * FROM qwe").fetchall()
    for i, j in result:
        a = j
    if a == 0:
        intro_text = ['                                           Игра govmomnongass',
            '',
            '                                           Чтобы прочитать правила нажми',
            '                                           кнопку Alt + F4',
            '',
            '                                           Тут будет написано за сколько',
            '                                           времени пройден уровень',
            '',
            '                                           Чтобы начать играть нажми',
            '                                           любую клавишу мыши']
    else:
        intro_text = ['                                           Игра govmomnongass',
            '',
            '                                           Чтобы прочитать правила нажми',
            '                                           кнопку Alt + F4',
            '',
            '                                В прошлый раз Уровень пройден за ' + str(a) + ' секунд',
            '',
            '                                           Чтобы начать играть нажми',
            '                                           любую клавишу мыши']
    con.commit()
    con.close()
    fon = pygame.transform.scale(load_image('fon.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 90
    for line in intro_text:
        string_rendered = font.render(line, True, pygame.Color('blue'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return None

        pygame.display.flip()


class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + WIN_WIDTH / 2, -t + WIN_HEIGHT / 2

    l = min(0, l)  # Не движемся дальше левой границы
    l = max(-(camera.width - WIN_WIDTH), l)  # Не движемся дальше правой границы
    t = max(-(camera.height - WIN_HEIGHT), t)  # Не движемся дальше нижней границы
    t = min(0, t)  # Не движемся дальше верхней границы

    return Rect(l, t, w, h)


def main():
    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("Amongausik")  # Пишем в шапку
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))  # Создание видимой поверхности
    # будем использовать как фон
    bg.fill(Color(BACKGROUND_COLOR))  # Заливаем поверхность сплошным цветом

    hero = Player(55, 55)  # создаем героя по (x,y) координатам
    left = right = False  # по умолчанию - стоим
    up = False

    entities = pygame.sprite.Group()  # Все объекты
    platforms = []  # то, во что мы будем врезаться или опираться

    entities.add(hero)

    level = [
        "--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",
        "-1     -                                                            -5    -                                       9                             -                                  '                                                                                                                                                                    [                                  -",
        "-      -               -----------                    ---------------     -                                  -   -                              - 8                            -------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                   -",
        "-      -              --2        -                  ----3           -     -                                  -   --------------------------------                                  ------------------------------------------------------------------------------------------------------------------------------------#                               -                                   -",
        "-      -                         -                 --               -     -        ---------------------------                                  -                                  ------------------------------------------------------------------------------------------------------------------------------------                                -                                   -",
        "-      -                         -                 --               -     -  -     7                         ---------------------------------- -                        ---       ------------------------------------------------------------------------------------------------------------------------------------                                -                                   -",
        "-      -                         -              -----               -     -  -                               -                                  -                                  ------------------------------------------------------------------------------------------------------------------------------------                                -                                   -",
        "-      -                         -              -          -------  -     -  -                               - ----------------------------------                                  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------                                   -",
        "-      -    ------------------   -              -          -        -     -z -                               -                                  -                                  -d~                                                                                                                                                                 -                                   -",
        "-      -                         -                         -        -     ---------------                    ---------------------------------- -                  ---             -                                                                                                                                                                   -                                   -",
        "-      -                         -----------------         -        -     -                                  -                                  -                                  -                                                                                                                                                                   -                                   -",
        "-      -                         -               -----------        -     -                                  -                                  -                                  -                                                                                                                                                                   -                                   -",
        "-      -        ------------------ ---------                        -     -                  -----------------                                  -                                  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------                                   -",
        "-~     -                         - -       -                        -     -                                  - -------------------------------- -            ---                   ---------------------------------------------------------------------------------------------------------------------------------------------------------------------                                   -",
        "-      -                         - -       -         ----------------~    ---------------                    -                         -6       -                                  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------                                   -",
        "-      -------                   - -       -----------              -           ------                       - -------------------------        -                                  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------                                   -",
        "-            --                  - -                        ------- -           ------                       -                         -        -                                  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------                                   -",
        "-                   ----         -                        ---     - -           ----------                   - -------------------------        -      ---                         ---------------------------------------------------------------------------------------------------------------------------------------------------------------------]                                  -",
        "-                                ---------              ---       - -                ---------               -                         -        -                                  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------                                   -",
        "-                                -       -------       --         - -                                        - -------------------------~       --------------------------------   ---------------------------------------------------------------------------------------------------------------------------------------------------------------------                                   -",
        "-                            -----             ----  ---            -                                ---------                         -        -                                  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------                                   -",
        "-                                -                ---    ------------                            -----       - ----------------------------------          ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                   -",
        "-                                -                                                             ---          z-                                                                     ---------------------------------------------------------------------------------------------------------------------------------------------------------------------                                   -",
        "--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"]

    timer = pygame.time.Clock()
    x = y = 0  # координаты
    for row in level:  # вся строка
        for col in row:  # каждый символ
            if col == "-":
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == "@":
                g = Gif(x, y)
                entities.add(g)
            if col == "z":
                g = Kaka(x, y)
                entities.add(g)
            if col == "1":
                g = Gifq(x, y)
                entities.add(g)
            if col == "2":
                g = Gifw(x, y)
                entities.add(g)
            if col == "3":
                g = Gife(x, y)
                entities.add(g)
            if col == "5":
                g = Gifr(x, y)
                entities.add(g)
            if col == "6":
                g = Gift(x, y)
                entities.add(g)
            if col == "7":
                g = Gify(x, y)
                entities.add(g)
            if col == "8":
                g = Gifu(x, y)
                entities.add(g)
            if col == "9":
                g = Gifi(x, y)
                entities.add(g)
            if col == "#":
                g = Gifo(x, y)
                entities.add(g)
            if col == "[":
                g = Gifp(x, y)
                entities.add(g)
            if col == "]":
                g = Gifa(x, y)
                entities.add(g)
            if col == "'":
                g = Gifs(x, y)
                entities.add(g)
            if col == "d":
                g = Gifd(x, y)
                entities.add(g)
            if col == "~":
                g = Giff(x, y)
                entities.add(g)
            x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля

    total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
    total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

    camera = Camera(camera_configure, total_level_width, total_level_height)
    i = 0
    j = 0
    running = True
    clock = pygame.time.Clock()

    while 1:  # Основной цикл программы
        timer.tick(60)
        for e in pygame.event.get():  # Обрабатываем события
            if e.type == QUIT:
                running = False
                a = clock.tick() // 1000
                if a == 0:
                    a += 1
                con = sqlite3.connect("qwe.db")
                cur = con.cursor()
                cur.execute('UPDATE qwe\n'
                            'SET vr = ?\n'
                            'WHERE id = "1"', (str(a), ))
                con.commit()
                con.close()

                raise SystemExit("Выход")
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False

        screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать

        for e in entities:
            screen.blit(e.image, camera.apply(e))
        camera.update(hero)  # центризируем камеру относительно персонажа
        hero.update(left, right, up, platforms)  # передвижение

        pygame.display.update()  # обновление и вывод всех изменений на экран


if __name__ == "__main__":
    start_screen()
    main()
