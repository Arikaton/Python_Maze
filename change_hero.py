import pygame as pg
from pyganim import *
from Amazing_Maze import main_game

DISPLAY = (900, 600)
WIDTH = 150
HEIGHT = 300

BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
XPEH = (254, 2, 231)

NEWTON = [('Sprites/Newton/newtonD1.png'), ('Sprites/Newton/newtonL1.png'), ('Sprites/Newton/newtonU1.png'), ('Sprites/Newton/newtonR1.png')]
Vitalya = [('Sprites/Vitalya/vf1.png'), ('Sprites/Vitalya/vl2.png'), ('Sprites/Vitalya/vb1.png'), ('Sprites/Vitalya/vr2.png')]
Sveta = [('Sprites/Sveta/sf1.png'), ('Sprites/Sveta/sl1.png'), ('Sprites/Sveta/sb1.png'), ('Sprites/Sveta/sr1.png')]
Marina = [('Sprites/Marina/mf1.png'), ('Sprites/Marina/ml1.png'), ('Sprites/Marina/mb1.png'), ('Sprites/Marina/mr1.png')]
config = open('config.txt', 'w')
config.write('default')
config.close()


class Character(pg.sprite.Sprite):
    def __init__(self, x, y, person, sprite, delay, name='default'):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.name = name
        self.image = pg.Surface((WIDTH, HEIGHT))
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        boltanim = []
        for anim in person:
            boltanim.append((pg.transform.scale(pg.image.load(anim), (WIDTH, HEIGHT)), delay))
        self.hero = PygAnimation(boltanim)
        self.hero.play()
        self.rect = self.image.get_rect(centerx=x, centery=y)
        self.sprite = font.render(sprite, 1, WHITE)
        self.sprite_rect = self.sprite.get_rect(centerx=x, y=self.rect.top-40)

    def update(self, screen):
        self.image.fill(BLACK)
        self.hero.blit(self.image, (0, 0))
        screen.blit(self.sprite, self.sprite_rect)

    def click(self, event, screen):
        if self.rect.collidepoint(event.pos):
            back_t = font.render('назад', 1, BLACK)
            back_rect = back_t.get_rect(centerx=120, y=DISPLAY[1]-80)
            go = font.render('выбрать', 1, BLACK)
            go_rect = go.get_rect(centerx=DISPLAY[0]-120, y=DISPLAY[1]-80)
            run = True

            while run:
                screen.blit(background, (0, 0))
                screen.blit(back_t, back_rect)
                screen.blit(go, go_rect)
                for e in pg.event.get():
                    if e.type == pg.QUIT:
                        exit()
                    if e.type == pg.MOUSEBUTTONDOWN:
                        if back_rect.collidepoint(e.pos):
                            run = False
                        if go_rect.collidepoint(e.pos):
                            config = open('config.txt', 'w')
                            config.write(self.name)
                            config.close()
                            return True
                    if e.type == pg.MOUSEMOTION:
                        if back_rect.collidepoint(e.pos):
                            back_t = font.render('назад', 1, RED)
                            screen.blit(back_t, back_rect)
                        if not back_rect.collidepoint(e.pos):
                            back_t = font.render('назад', 1, BLACK)
                            screen.blit(back_t, back_rect)
                        if go_rect.collidepoint(e.pos):
                            go = font.render('выбрать', 1, RED)
                            screen.blit(go, go_rect)
                        if not go_rect.collidepoint(e.pos):
                            go = font.render('выбрать', 1, BLACK)
                            screen.blit(go, go_rect)
                pg.display.update()
                pg.time.delay(10)
            choose()


def choose():
    pg.init()
    global font, background
    font = pg.font.Font(None, 80)
    time = pg.time.Clock()
    screen = pg.display.set_mode(DISPLAY)
    background = pg.transform.scale(pg.image.load('Sprites/Background/main_menu.png'), DISPLAY)
    screen.blit(background, (0, 0))
    pg.display.update()

    arrow = pg.image.load('Sprites/arrow.png')
    arrowr = pg.image.load('Sprites/arrowr.png')
    arrow_rect = arrow.get_rect(centerx=DISPLAY[0]/2, y=40)
    arrow_color = True


    my_mother = Character(150, 300, Sveta,"Света", 500, 'sveta')
    my_father = Character(DISPLAY[0] / 2, 300, Vitalya, "Виталя", 500, 'vitalya')
    my_marina = Character(750, 300, Marina, "Марина", 500, 'marina')
    alina_mother = Character(150, 300, NEWTON, "Татьяна", 500)
    alina_father = Character(DISPLAY[0]/2, 300, NEWTON, "Женя", 1000)
    alina_else = Character(750, 300, NEWTON, "уто-то", 500)

    characters = pg.sprite.Group()
    characters.add(my_father, my_marina, my_mother)
    characters2 = pg.sprite.Group()
    characters2.add(alina_mother, alina_father, alina_else)
    cur_char = characters

    back = font.render('назад', 1, BLACK)
    back_rect = back.get_rect(centerx=DISPLAY[0]-120, y=DISPLAY[1]-80)
    screen.blit(back, back_rect)
    screen.blit(arrow, arrow_rect)
    next = True

    while 1:
        screen.blit(background, (0, 0))
        screen.blit(back, back_rect)
        screen.blit(arrow, arrow_rect)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                for person in cur_char:
                    person.click(event, screen)
                if back_rect.collidepoint(event.pos):
                    main_game.main_menu()
                if arrow_rect.collidepoint(event.pos):
                    if next:
                        next = False
                    else:
                        next = True
            if event.type == pg.MOUSEMOTION:
                if back_rect.collidepoint(event.pos):
                    back = font.render('назад', 1, RED)
                    screen.blit(back, back_rect)
                if not back_rect.collidepoint(event.pos):
                    back = font.render('назад', 1, BLACK)
                    screen.blit(back, back_rect)
                if arrow_rect.collidepoint(event.pos):
                    arrow_color = False
                if not arrow_rect.collidepoint(event.pos):
                    arrow_color = True
        if next:
            cur_char = characters
            characters.update(screen)
            for e in characters:
                screen.blit(e.image, e.rect)
        if not next:
            cur_char = characters2
            characters2.update(screen)
            for e in characters2:
                screen.blit(e.image, e.rect)
        if arrow_color:
            screen.blit(arrow, arrow_rect)
        elif not arrow_color:
            screen.blit(arrowr, arrow_rect)
        pg.display.update()
        time.tick(60)








