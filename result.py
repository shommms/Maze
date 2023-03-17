from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = "left"

    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= win_width - 85:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load(
    "img/background3.png"), (win_width, win_height))

player = Player('img/hero.png', 5, win_height - 80, 4)
monster = Enemy('img/cyborg.png', win_width - 80, 280, 2)
final = GameSprite('img/treasure.png', win_width - 120, win_height - 80, 0)

w1 = Wall(139, 0, 255, 100, 100, 450, 50)
w2 = Wall(139, 0, 255, 100, 100, 10, 350)
w3 = Wall(139, 0, 255, 10, 10, 10, 400)
w4 = Wall(139, 0, 255, 10, 10, 640, 10)
w5 = Wall(139, 0, 255, 640, 10, 10, 260)
w6 = Wall(139, 0, 255, 540, 230, 10, 50)
w7 = Wall(139, 0, 255, 200, 230, 340, 10)
w8 = Wall(139, 0, 255, 200, 230, 10, 160)
w9 = Wall(139, 0, 255, 200, 390, 350, 10)
w10 = Wall(139, 0, 255, 540, 340, 10, 80)
w11 = Wall(139, 0, 255, 640, 340, 10, 80)
w12 = Wall(139, 0, 255, 470, 270, 70, 10)
w13 = Wall(139, 0, 255, 470, 340, 70, 10)
w14 = Wall(139, 0, 255, 460, 270, 10, 80)
w15 = Wall(139, 0, 255, 650, 340, 30, 10)
w16 = Wall(139, 0, 255, 640, 270, 40, 10)
w17 = Wall(139, 0, 255, 680, 270, 10, 80)

game = True
finish = False
clock = time.Clock()
FPS = 60

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))

mixer.init()
mixer.music.load('music/jungles.ogg')
mixer.music.play()

money = mixer.Sound('music/money.ogg')
kick = mixer.Sound('music/kick.ogg')

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0, 0))
        player.update()
        monster.update()

        player.reset()
        monster.reset()
        final.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()
        w11.draw_wall()
        w12.draw_wall()
        w13.draw_wall()
        w14.draw_wall()
        w15.draw_wall()
        w16.draw_wall()
        w17.draw_wall()

    if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7) or sprite.collide_rect(player, w8) or sprite.collide_rect(player, w8) or sprite.collide_rect(player, w10) or sprite.collide_rect(player, w11) or sprite.collide_rect(player, w12) or sprite.collide_rect(player, w13) or sprite.collide_rect(player, w14) or sprite.collide_rect(player, w15) or sprite.collide_rect(player, w16) or sprite.collide_rect(player, w17):
        finish = True
        window.blit(lose, (200, 200))
        kick.play()

    if sprite.collide_rect(player, final):
        finish = True
        window.blit(win, (200, 200))
        money.play()

    display.update()
    clock.tick(FPS)
