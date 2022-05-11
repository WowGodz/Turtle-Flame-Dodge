import pygame, sys
from pygame.locals import *

mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
height = 680
width = 920
clock = pygame.time.Clock()
clock.tick()
fps = int(clock.get_fps())
a = (fps / 60) * 100
if a >= 100:
    a = 60
pygame.display.set_caption('Turtle Flame Dodge                                                                        '
                           '                                                                                         '
                           '  FPS: 60')
window = pygame.display.set_mode((800, 480))
font = pygame.font.SysFont(None, 20)
font1 = pygame.font.SysFont("comicsan", 30, True)
font = pygame.font.SysFont("arial", 30, True)
text = font.render('asdasd', 1, (213, 190, 30))
bg_img = pygame.image.load('bg.png')
bg = pygame.transform.scale(bg_img, (width + 100, height))
start_img = pygame.image.load('start.png')
start = pygame.transform.scale(start_img, (200, 200))
pause_img = pygame.image.load('pause.png')
pause = pygame.transform.scale(pause_img, (width + 100, height))
kill = 0
keys = pygame.key.get_pressed()


def redrawGameWindow():
    window.blit(bg, (0, 0))


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    window.blit(textobj, textrect)


click = False


def main_menu():
    global click
    while True:
        clock = pygame.time.Clock()
        clock.tick(60)
        redrawGameWindow()
        fps = int(clock.get_fps())
        a = (fps / 60) * 100
        if a >= 100:
            a = 60
        draw_text('Turtle Flame Dodge', font, (255, 255, 255), window, 20, 20)
        draw_text('Game Paused, Click To START', font1, (25, 65, 165), window, 30, 70)

        mx, my = pygame.mouse.get_pos()
        window.blit(start, (300, 180))
        button_1 = pygame.Rect(300, 180, 200, 200)

        if button_1.collidepoint((mx, my)):
            if click or keys[pygame.K_SPACE]:
                game()
        pygame.display.update()
        if keys[pygame.K_SPACE]:
            game()
        # pygame.draw.rect(window, (255, 123, 20), button_1)
        window.blit(start, (300, 180))
        draw_text('', font1, (25, 65, 165), window, 355, 215)
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def game():
    running = True
    while running:
        import pygame
        import sys
        import time

        pygame.init()
        height = 680
        width = 920
        win = pygame.display.set_mode((width, height))
        bg_img = pygame.image.load('bg.png')
        bg = pygame.transform.scale(bg_img, (width + 100, height))
        player1 = pygame.image.load('turtle.png')
        player1 = pygame.transform.scale(player1, (40, 40))
        wall = pygame.image.load('wall.png')
        wall = pygame.transform.scale(wall, (40, 200))
        pause_img = pygame.image.load('pause.png')
        pause = pygame.transform.scale(pause_img, (width + 100, height))
        width = 1000
        i = 0

        goRight = [player1, player1]
        goLeft = [player1, player1]
        goWall = [wall]

        class player(object):
            def __init__(self, x, y, w, h):
                self.right = False
                self.left = False
                self.standing = True
                self.isJump = False
                self.numWalk = 0
                self.numJump = 10
                self.x = x
                self.y = y
                self.w = w
                self.h = h
                self.vel = 10
                self.hitbox = (self.x, self.y, self.w, self.h)

            def draw(self):
                if self.numWalk + 1 >= 4:
                    self.numWalk = 0

                if not self.standing:
                    if self.left:
                        win.blit(goLeft[self.numWalk // 3], (self.x, self.y))
                        self.numWalk += 1
                    elif self.right:
                        win.blit(goRight[self.numWalk // 3], (self.x, self.y))
                        self.numWalk += 1
                else:
                    if self.right:
                        win.blit(goRight[0], (self.x, self.y))
                    else:
                        win.blit(goLeft[0], (self.x, self.y))

                # pygame.draw.rect(win, (60, 190, 255), (self.x, self.y, self.w, self.h))  # player
                self.hitbox = (self.x, self.y, self.w, self.h)
                # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

            def hit(self):
                self.isJump = False
                self.numJump = 10
                self.x = 60
                self.y = 410
                self.numWalk = 0
                font = pygame.font.SysFont("comicsan", 50, True)
                text = font.render('You lost', 1, (213, 190, 30))
                win.blit(text, (250 - (text.get_width() / 2), 100))
                pygame.display.update()
                i = 0
                while i < 300:
                    pygame.time.delay(10)
                    i += 1
                    main_menu()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            i = 301
                            pygame.quit()

        class screen1(object):  # hitbox for the screen if you were to die by hitting the floor or ceiling
            def __init__(self, x, y, w, h):
                self.x = x
                self.y = y
                self.w = w
                self.h = h
                self.vel = 10
                self.hitbox = (self.x, self.y, self.w, self.h)

            def draw(self):
                pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.w, self.h), 2)  # BOT
                self.hitbox = (self.x, self.y, self.w, self.h)

        class bot(object):
            def __init__(self, x, y, w, h):
                self.right = False
                self.left = False
                self.standing = True
                self.x = x
                self.y = y
                self.w = w
                self.h = h
                self.numWalk = 0
                self.vel = 10
                self.hitbox = (self.x, self.y, self.w, self.h)

            def draw(self):
                if self.numWalk + 1 >= 4:
                    self.numWalk = 0

                if not self.standing:
                    if self.left:
                        win.blit(goWall[self.numWalk // 3], (self.x, self.y))
                        self.numWalk += 1
                    elif self.right:
                        win.blit(goWall[self.numWalk // 3], (self.x, self.y))
                        self.numWalk += 1
                else:
                    if self.right:
                        win.blit(goWall[0], (self.x, self.y))
                    else:
                        win.blit(goWall[0], (self.x, self.y))

                # pygame.draw.rect(win, (60, 190, 255), (self.x, self.y, self.w, self.h))  # BOT
                self.hitbox = (self.x + 7, self.y + 10, self.w - 10, self.h - 15)
                q = 0
                if keys[pygame.K_SPACE] and q == 0:
                    q = 100
                elif keys[pygame.K_SPACE] and q == 100:
                    q = 0
                if q == 100:
                    pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

        def controls():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                player.x += player.vel
                player.left = False
                player.right = True
                player.standing = False
            if keys[pygame.K_LEFT]:
                player.x -= player.vel
                player.left = True
                player.right = False
                player.standing = False
            if keys[pygame.K_UP]:
                player.y -= player.vel
                player.right = True
                player.left = False
                player.standing = False
            if keys[pygame.K_DOWN]:
                player.y += player.vel
                player.right = True
                player.left = False
                player.standing = False
            if not keys[pygame.K_UP] and player.x < width / 3:
                neg = -1
                bot.x += (player.numJump ** 2) * 0.025 * neg
                bot2.x += (player.numJump ** 2) * 0.025 * neg
                player.numJump -= 0.1

        def law():
            if player.x == 0:
                player.x = 910
            if player.x == 920:
                player.x = 0
            if player.y == 0:
                player.y = 660
            if player.y == 680:
                player.y = 0

            bot.x -= 2  # Wall Top #1
            bot2.x -= 2  # Wall bottom #1
            bot2_3.x -= 2  # Wall bottom #2
            bot1_2.x -= 2  # Wall Top #2
            bot2_4.x -= 2  # Wall bottom #3
            bot1_3.x -= 2  # Wall Top #3
            bot.y -= 2  # Wall Top #1
            bot2.y -= 2  # Wall bottom #1
            bot2_3.y -= 2  # Wall bottom #2
            bot1_2.y -= 2  # Wall Top #2
            bot2_4.y -= 2  # Wall bottom #3
            bot1_3.y -= 2  # Wall Top #3

            # Wall Top #1
            if bot.x < screen1.x:
                bot.x = 910

            if bot.y < screen1.y:
                bot.y = 680

            # Wall bottom #1
            if bot2.x < screen1.x:
                bot2.x = 910

            if bot2.y < screen1.y:
                bot2.y = 680

            # Wall Top #2
            if bot1_2.x < screen1.x:
                bot1_2.x = 910

            if bot1_2.y < screen1.y:
                bot1_2.y = 680

            # Wall Top #3
            if bot1_3.x < screen1.x:
                bot1_3.x = 910

            if bot1_3.y < screen1.y:
                bot1_3.y = 680

            # Wall bottom #2
            if bot2_3.x < screen1.x:
                bot2_3.x = 910

            # Wall bottom #3
            if bot2_4.y < screen1.y:
                bot2_4.y = 910

        def hitbox():
            fps = int(clock.get_fps())
            a = (fps / 60) * 100
            if a >= 100:
                a = 60
            if player.hitbox[1] < bot.hitbox[1] + bot.hitbox[3] and player.hitbox[1] + \
                    player.hitbox[
                        3] > \
                    bot.hitbox[1]:  # Hitbox for Wall Top #1
                if player.hitbox[0] + player.hitbox[2] > bot.hitbox[0] and player.hitbox[0] < \
                        bot.hitbox[0] + bot.hitbox[2]:
                    player.hit()
                    print("player hit wall 1 T")

            if player.hitbox[1] < bot1_2.hitbox[1] + bot1_2.hitbox[3] and player.hitbox[1] + \
                    player.hitbox[
                        3] > \
                    bot1_2.hitbox[1]:  # Hitbox for Wall Top #2
                if player.hitbox[0] + player.hitbox[2] > bot1_2.hitbox[0] and player.hitbox[0] < \
                        bot1_2.hitbox[0] + bot1_2.hitbox[2]:
                    player.hit()
                    print("player hit wall 2 T")

            if player.hitbox[1] < bot2.hitbox[1] + bot2.hitbox[3] and player.hitbox[1] + \
                    player.hitbox[
                        3] > \
                    bot2.hitbox[1]:  # Hitbox for # Wall bottom #1
                if player.hitbox[0] + player.hitbox[2] > bot2.hitbox[0] and player.hitbox[0] < \
                        bot2.hitbox[0] + bot2.hitbox[2]:
                    player.hit()
                    print("player hit wall 1 B")
            if player.hitbox[1] < bot2_3.hitbox[1] + bot2_3.hitbox[3] and player.hitbox[1] + \
                    player.hitbox[
                        3] > \
                    bot2_3.hitbox[1]:  # Hitbox for # Wall bottom #2
                if player.hitbox[0] + player.hitbox[2] > bot2_3.hitbox[0] and player.hitbox[0] < \
                        bot2_3.hitbox[0] + bot2_3.hitbox[2]:
                    player.hit()
                    print("player hit wall 2 B")
            if player.hitbox[1] < bot1_3.hitbox[1] + bot1_3.hitbox[3] and player.hitbox[1] + \
                    player.hitbox[
                        3] > \
                    bot1_3.hitbox[1]:  # Hitbox for # Wall top #3
                if player.hitbox[0] + player.hitbox[2] > bot1_3.hitbox[0] and player.hitbox[0] < \
                        bot1_3.hitbox[0] + bot1_3.hitbox[2]:
                    player.hit()
                    print("player hit wall 3 T")
            if player.hitbox[1] < bot2_4.hitbox[1] + bot2_4.hitbox[3] and player.hitbox[1] + \
                    player.hitbox[
                        3] > \
                    bot2_4.hitbox[1]:  # Hitbox for # Wall bottom #3
                if player.hitbox[0] + player.hitbox[2] > bot2_4.hitbox[0] and player.hitbox[0] < \
                        bot2_4.hitbox[0] + bot2_4.hitbox[2]:
                    player.hit()
                    print("player hit wall 3 B")
            if player.hitbox[1] < screen1.hitbox[1] + screen1.hitbox[3] and player.hitbox[1] + \
                    player.hitbox[
                        3] > \
                    screen1.hitbox[1]:  # screen
                if player.hitbox[0] + player.hitbox[2] > screen1.hitbox[0] and player.hitbox[0] < \
                        screen1.hitbox[0] + screen1.hitbox[2]:
                    if clock.get_fps() > 59.9:
                        print(a)

            # bot2_4 = bot(500 * 2, 620, 40, 200)  # Wall bottom #3
            # bot1_3 = bot(500 * 2, 0, 40, 200)  # Wall top #3
            # bot2_3 = bot(500 * 1.5, 620, 40, 200)  # Wall bottom #2
            # bot1_2 = bot(500 * 1.5, 0, 40, 200)  # Wall top #2
            #  bot2 = bot(500, 620, 40, 200)  # Wall bottom #1
            #  bot = bot(500, 0, 40, 200)  # Wall top #1

            if player.x < screen1.x - player.vel:
                player.hit()

        def score():
            secs = int(0)
            for i in range(secs):
                print("score: ", secs - i)
                time.sleep(1)

        def redraw():
            screen1.draw()
            player.draw()
            bot.draw()
            bot2.draw()
            bot2_3.draw()
            bot1_2.draw()
            bot2_4.draw()
            bot1_3.draw()
            controls()
            law()
            hitbox()
            score()


        player = player(10, 310, 40, 40)
        # Bot are walls
        bot2_4 = bot(500 * 2, 620, 40, 200)  # Wall bottom #3
        bot1_3 = bot(500 * 2, 0, 40, 200)  # Wall top #3
        bot2_3 = bot(500 * 1.5, 620, 40, 200)  # Wall bottom #2
        bot1_2 = bot(500 * 1.5, 0, 40, 200)  # Wall top #2
        bot2 = bot(500, 320, 40, 200)  # Wall bottom #1
        bot = bot(500, 0, 40, 200)  # Wall top #1
        screen1 = screen1(0, 0, 920, 680)

        clock = pygame.time.Clock()
        run = True
        while run:
            keys = pygame.key.get_pressed()
            win.fill((0, 0, 0))

            # Create looping background
            win.blit(bg, (i, 0))
            win.blit(bg, (width + i, 0))
            if i == -width:
                win.blit(bg, (width + i, 0))
                i = 0
            i -= 1
            clock.tick(60)  # FPS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            redraw()  # Events
            death = 0
            if hitbox():
                death += 1
                if death == 1:
                    main_menu()
                else:
                    death = 0

            pygame.display.update()

        pygame.quit()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False


main_menu()
