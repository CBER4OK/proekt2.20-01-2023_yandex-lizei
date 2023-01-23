from pygame import *
import os

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"
ICON_DIR = os.path.dirname(__file__)  # Полный путь к каталогу с файлами
GIF_WIDTH = 1088
GIF_HEIGHT = 704


class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.image = image.load("%s/blocks/platform.png" % ICON_DIR)
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


class Gif(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image = image.load("%s/gifk/4A5.gif" % ICON_DIR)
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


class Kaka(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((GIF_WIDTH, GIF_HEIGHT))
        self.image = image.load("%s/gifk/govno.jpg" % ICON_DIR)
        self.rect = Rect(x, y, GIF_WIDTH, GIF_HEIGHT)


class Gifq(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((GIF_WIDTH, GIF_HEIGHT))
        self.image = image.load("%s/gifk/krot.jpg" % ICON_DIR)
        self.rect = Rect(x, y, GIF_WIDTH, GIF_HEIGHT)


class Gifw(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((GIF_WIDTH, GIF_HEIGHT))
        self.image = image.load("%s/gifk/vsem_dobra.jpg" % ICON_DIR)
        self.rect = Rect(x, y, GIF_WIDTH, GIF_HEIGHT)


class Gife(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((GIF_WIDTH, GIF_HEIGHT))
        self.image = image.load("%s/gifk/baba.jpg" % ICON_DIR)
        self.rect = Rect(x, y, GIF_WIDTH, GIF_HEIGHT)


class Gifr(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((GIF_WIDTH, GIF_HEIGHT))
        self.image = image.load("%s/gifk/ahaha.jpg" % ICON_DIR)
        self.rect = Rect(x, y, GIF_WIDTH, GIF_HEIGHT)


class Gift(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((GIF_WIDTH, GIF_HEIGHT))
        self.image = image.load("%s/gifk/smeh.jpg" % ICON_DIR)
        self.rect = Rect(x, y, GIF_WIDTH, GIF_HEIGHT)


class Gify(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((GIF_WIDTH, GIF_HEIGHT))
        self.image = image.load("%s/gifk/banan.jpg" % ICON_DIR)
        self.rect = Rect(x, y, GIF_WIDTH, GIF_HEIGHT)


class Gifu(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((GIF_WIDTH, GIF_HEIGHT))
        self.image = image.load("%s/gifk/ahahah.jpg" % ICON_DIR)
        self.rect = Rect(x, y, GIF_WIDTH, GIF_HEIGHT)


class Gifi(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((GIF_WIDTH, GIF_HEIGHT))
        self.image = image.load("%s/gifk/smech.jpg" % ICON_DIR)
        self.rect = Rect(x, y, GIF_WIDTH, GIF_HEIGHT)


class Gifo(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((GIF_WIDTH, GIF_HEIGHT))
        self.image = image.load("%s/gifk/terpila.jpg" % ICON_DIR)
        self.rect = Rect(x, y, GIF_WIDTH, GIF_HEIGHT)


class Gifp(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((GIF_WIDTH, GIF_HEIGHT))
        self.image = image.load("%s/gifk/4A5.gif" % ICON_DIR)
        self.rect = Rect(x, y, GIF_WIDTH, GIF_HEIGHT)


class Gifa(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((GIF_WIDTH, GIF_HEIGHT))
        self.image = image.load("%s/gifk/ura.jpg" % ICON_DIR)
        self.rect = Rect(x, y, GIF_WIDTH, GIF_HEIGHT)


class Gifs(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((GIF_WIDTH, GIF_HEIGHT))
        self.image = image.load("%s/gifk/hohol.jpg" % ICON_DIR)
        self.rect = Rect(x, y, GIF_WIDTH, GIF_HEIGHT)


class Gifd(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((GIF_WIDTH, GIF_HEIGHT))
        self.image = image.load("%s/gifk/rusia.jpg" % ICON_DIR)
        self.rect = Rect(x, y, GIF_WIDTH, GIF_HEIGHT)


class Giff(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((GIF_WIDTH, GIF_HEIGHT))
        self.image = image.load("%s/gifk/zag.jpg" % ICON_DIR)
        self.rect = Rect(x, y, GIF_WIDTH, GIF_HEIGHT)
