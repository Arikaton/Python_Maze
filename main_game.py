import pygame as pg
import pyganim
from Amazing_Maze import Walls, Player, change_hero
from tiledtmxloader import tmxreader, helperspygame
from Amazing_Maze import image_parser

WIN_WIDTH = 950
WIN_HEIGHT = 600
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
WALL_WIDTH = 32
WALL_HEIGHT = 32

FILE_DIR = 'Levels'

test_lvl = image_parser.pars('Levels/level.png')
for i in range(len(test_lvl[0])):
    if test_lvl[0][i] == ' ':
        startx = i
    if test_lvl[-1][i] == ' ':
        finishx = i


def main_menu():
    pg.init()
    global screen, time, font

    font = pg.font.Font(None, 80)
    play = font.render('Играть', 1, (255, 255, 255))
    play_rect = play.get_rect(centerx=WIN_WIDTH/2, y=100)
    change_character = font.render('Выбрать игрока', 1, (255, 255, 255))
    change_character_rect = change_character.get_rect(centerx=WIN_WIDTH/2, y=200)
    exit = font.render('Выход', 1, (255, 255, 255))
    exit_rect = exit.get_rect(centerx=WIN_WIDTH/2, y=300)

    screen = pg.display.set_mode(DISPLAY)
    pg.display.set_caption('AMAZING MAZE')
    time = pg.time.Clock()
    background = pg.transform.scale(pg.image.load('Sprites/Background/main_menu.png'), (WIN_WIDTH, WIN_HEIGHT))
    screen.blit(background, (0, 0))
    screen.blit(play, play_rect)
    screen.blit(change_character, change_character_rect)
    screen.blit(exit, exit_rect)
    pg.display.update()
    running = True
    choose = False
    play_v = False

    while running:
        screen.blit(background, (0, 0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_g:
                    main()
            if event.type == pg.MOUSEMOTION:
                if play_rect.collidepoint(event.pos):
                    play = font.render('Играть', 1, (255, 0, 0))
                    screen.blit(play, play_rect)
                elif not play_rect.collidepoint(event.pos):
                    play = font.render('Играть', 1, (255, 255, 255))
                    screen.blit(play, play_rect)
                if change_character_rect.collidepoint(event.pos):
                    change_character = font.render('Выбрать игрока', 1, (255, 0, 0))
                    screen.blit(change_character, change_character_rect)
                elif not change_character_rect.collidepoint(event.pos):
                    change_character = font.render('Выбрать игрока', 1, (255, 255, 255))
                    screen.blit(change_character, change_character_rect)
                if exit_rect.collidepoint(event.pos):
                    exit = font.render('Выход', 1, (255, 0, 0))
                    screen.blit(exit, exit_rect)
                elif not exit_rect.collidepoint(event.pos):
                    exit = font.render('Выход', 1, (255, 255, 255))
                    screen.blit(exit, exit_rect)
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if play_rect.collidepoint(event.pos):
                        play_v = True
                        running = False
                    if exit_rect.collidepoint(event.pos):
                        exit()
                    if change_character_rect.collidepoint(event.pos):
                        choose = True
                        running = False
        screen.blit(play, play_rect)
        screen.blit(change_character, change_character_rect)
        screen.blit(exit, exit_rect)
        pg.display.update()
        time.tick(60)

    if choose:
        change_hero.choose()
    if play_v:
        main()


class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pg.Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l+WIN_WIDTH / 2, -t + WIN_HEIGHT / 2

    l = min(0, l)
    l = max(-(camera.width-WIN_WIDTH), l)
    t = max(-(camera.height-WIN_HEIGHT), t)
    t = min(0, t)
    return pg.Rect(l, t, w, h)


def finish_game():
    finish1 = font.render('Поздравляю,', 1, (255, 255, 255))
    finish2 = font.render('Вы выиграли!', 1, (255, 255, 255))
    finish3 = font.render('Держите ваш подарок', 1, (255, 255, 255))

    finish_rect1 = finish1.get_rect(centerx=WIN_WIDTH/2, centery=WIN_HEIGHT/2-160)
    finish_rect2 = finish2.get_rect(centerx=WIN_WIDTH / 2, centery=WIN_HEIGHT / 2 - 80)
    finish_rect3 = finish3.get_rect(centerx=WIN_WIDTH / 2, centery=WIN_HEIGHT / 2)
    background = pg.transform.scale(pg.image.load('Sprites/Background/main_menu.png'), (WIN_WIDTH, WIN_HEIGHT))
    screen.blit(background, (0, 0))
    screen.blit(finish1, finish_rect1)
    screen.blit(finish2, finish_rect2)
    screen.blit(finish3, finish_rect3)


def main():
    config = open('config.txt')
    name = config.read()
    config.close()
    walls = []
    road = pg.sprite.Group()
    #anim_object = pg.sprite.Group()
    entities = pg.sprite.Group()
    hero = Player.Hero(32*startx, 0, name)
    gift = Walls.Gift(32*finishx, len(test_lvl)*32-32)
    left, right, up, down = False, False, False, False

    x, y = 0, 0
    for row in test_lvl:
        for col in row:
            if col == ' ':
                rd = Walls.Road(x, y, test_lvl)
                road.add(rd)
                entities.add(rd)
                screen.blit(rd.image, (x, y))
            if col == '*':
                ww = Walls.WoodWall(x, y)
                entities.add(ww)
                walls.append(ww)
                #anim_object.add(aw)

            x += WALL_WIDTH
        x = 0
        y += WALL_HEIGHT
    entities.add(hero)
    entities.add(gift)

    total_level_width = len(test_lvl[0])*WALL_WIDTH
    total_level_height = len(test_lvl)*WALL_HEIGHT

    camera = Camera(camera_configure, total_level_width, total_level_height)

    while 1:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                exit()
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_f:
                    coor = hero.rect.topleft
                if e.key == pg.K_r:
                    hero.rect.topleft = coor
                if e.key == pg.K_LEFT:
                    left = True
                if e.key == pg.K_RIGHT:
                    right = True
                if e.key == pg.K_UP:
                    up = True
                if e.key == pg.K_DOWN:
                    down = True
                if e.key == pg.K_y:
                    main()
                    break
                if e.key == pg.K_n:
                    main_menu()
                    break
            if e.type == pg.KEYUP:
                if e.key == pg.K_LEFT:
                    left = False
                if e.key == pg.K_RIGHT:
                    right = False
                if e.key == pg.K_UP:
                    up = False
                if e.key == pg.K_DOWN:
                    down = False

        hero.update(left, right, up, down, walls)

        camera.update(hero)
        for e in entities:
            screen.blit(e.image, camera.apply(e))
        #anim_object.update()
        if gift.rect.colliderect(hero.rect):
            finish_game()
        pg.display.update()
        time.tick(60)


if __name__ == '__main__':
    main_menu()