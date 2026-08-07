import pygame
import sys

pygame.init()

# Window
WIDTH = 1000
HEIGHT = 550

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Naruto Kunai - Mayuri Biryani")

clock = pygame.time.Clock()


# Colors
SKY = (120, 200, 255)
GRASS = (70, 170, 70)
BLACK = (20, 20, 20)
ORANGE = (255, 140, 0)
BLUE = (40, 80, 220)
SKIN = (255, 210, 170)
GRAY = (120, 120, 120)
RED = (220, 50, 50)
BROWN = (130, 70, 30)
YELLOW = (255, 220, 0)
WHITE = (255, 255, 255)
RICE = (245, 230, 170)
CHICKEN = (170, 80, 30)
GREEN = (40, 160, 40)


# Player (Naruto)
player = pygame.Rect(120, 350, 60, 100)

player_speed = 6
facing_right = True


# Kunai
kunais = []


# Mayuri shop
shop = pygame.Rect(760, 270, 150, 180)

shop_hp = 10


# Explosion and biryani
shop_destroyed = False
pieces = []

biryani = False
biryani_broken = False
game_over = False



def draw_ninja(x, y):

    pygame.draw.ellipse(
        screen,
        BLACK,
        (x, y + 95, 60, 10)
    )

    pygame.draw.line(
        screen,
        BLACK,
        (x+20, y+75),
        (x+10, y+105),
        6
    )

    pygame.draw.line(
        screen,
        BLACK,
        (x+40, y+75),
        (x+50, y+105),
        6
    )


    pygame.draw.rect(
        screen,
        ORANGE,
        (x+10, y+35, 40, 45)
    )


    pygame.draw.circle(
        screen,
        SKIN,
        (x+30, y+20),
        22
    )


    pygame.draw.polygon(
        screen,
        BLACK,
        [
            (x+10,y+10),
            (x+30,y-5),
            (x+55,y+10)
        ]
    )


    pygame.draw.rect(
        screen,
        BLUE,
        (x+8,y+15,44,8)
    )


    pygame.draw.circle(
        screen,
        BLACK,
        (x+22,y+22),
        3
    )

    pygame.draw.circle(
        screen,
        BLACK,
        (x+38,y+22),
        3
    )



def draw_shop():

    pygame.draw.rect(
        screen,
        BROWN,
        shop
    )


    pygame.draw.polygon(
        screen,
        RED,
        [
            (shop.x-20,shop.y),
            (shop.x+75,shop.y-70),
            (shop.x+170,shop.y)
        ]
    )


    pygame.draw.rect(
        screen,
        BLACK,
        (shop.x+55,shop.y+70,40,80)
    )


    pygame.draw.rect(
        screen,
        YELLOW,
        (shop.x+20,shop.y+15,110,35)
    )


    font = pygame.font.Font(None,30)

    text = font.render(
        "MAYURI",
        True,
        BLACK
    )

    screen.blit(
        text,
        (shop.x+35,shop.y+22)
    )


    # black health bar

    pygame.draw.rect(
        screen,
        BLACK,
        (shop.x,shop.y-35,150,15)
    )


    pygame.draw.rect(
        screen,
        RED,
        (shop.x,shop.y-35,shop_hp*15,15)
    )
def draw_kunai(x, y):

    pygame.draw.line(
        screen,
        GRAY,
        (x,y),
        (x+20,y),
        5
    )

    pygame.draw.polygon(
        screen,
        BLACK,
        [
            (x+25,y),
            (x+10,y-8),
            (x+10,y+8)
        ]
    )



def explode_shop():

    global pieces

    for i in range(35):

        pieces.append(
            [
                shop.x+75,
                shop.y+90,
                (i % 7)-3,
                -10-(i % 4)
            ]
        )



def draw_biryani():

    global game_over


    # If broken

    if biryani_broken:

        # split bowl pieces

        pygame.draw.arc(
            screen,
            WHITE,
            (770,350,60,80),
            1.5,
            4.7,
            6
        )

        pygame.draw.arc(
            screen,
            WHITE,
            (860,350,60,80),
            -1.5,
            1.7,
            6
        )


        # Rice scattered

        for x,y in [
            (800,380),
            (880,390),
            (830,410),
            (900,370)
        ]:

            pygame.draw.circle(
                screen,
                RICE,
                (x,y),
                6
            )


        font = pygame.font.Font(None,70)

        text = font.render(
            "GAME OVER",
            True,
            RED
        )

        screen.blit(
            text,
            (330,200)
        )


    else:

        # Bowl shadow

        pygame.draw.ellipse(
            screen,
            BLACK,
            (780,420,140,20)
        )


        # Bowl

        pygame.draw.ellipse(
            screen,
            WHITE,
            (790,350,120,80)
        )


        # Rice

        for x,y in [
            (810,370),
            (830,360),
            (850,375),
            (870,365),
            (820,395),
            (850,400),
            (880,390)
        ]:

            pygame.draw.circle(
                screen,
                RICE,
                (x,y),
                8
            )


        # Chicken pieces

        for x,y in [
            (820,375),
            (860,385),
            (845,360)
        ]:

            pygame.draw.circle(
                screen,
                CHICKEN,
                (x,y),
                7
            )


        # Green garnish

        for x,y in [
            (810,360),
            (875,375),
            (840,405)
        ]:

            pygame.draw.circle(
                screen,
                GREEN,
                (x,y),
                3
            )


        # Steam

        pygame.draw.arc(
            screen,
            WHITE,
            (815,315,25,45),
            0,
            3.14,
            3
        )

        pygame.draw.arc(
            screen,
            WHITE,
            (855,315,25,45),
            0,
            3.14,
            3
        )


        font = pygame.font.Font(None,40)

        text = font.render(
            "BIRYANI!",
            True,
            RED
        )

        screen.blit(
            text,
            (780,280)
        )
# Main game loop

running = True

while running:

    screen.fill(SKY)


    # Ground

    pygame.draw.rect(
        screen,
        GRASS,
        (0,450,WIDTH,100)
    )


    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()
            sys.exit()


        # Throw kunai

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE and not game_over:

                direction = 1 if facing_right else -1

                kunais.append(
                    [
                        player.x+60,
                        player.y+45,
                        direction
                    ]
                )



    # Movement

    if not game_over:

        keys = pygame.key.get_pressed()


        if keys[pygame.K_RIGHT]:

            player.x += player_speed
            facing_right = True


        if keys[pygame.K_LEFT]:

            player.x -= player_speed
            facing_right = False



    player.x = max(
        0,
        min(WIDTH-60, player.x)
    )



    # Move kunais

    for k in kunais[:]:


        k[0] += k[2]*15


        draw_kunai(
            k[0],
            k[1]
        )


        hitbox = pygame.Rect(
            k[0],
            k[1]-5,
            30,
            10
        )


        # Hit Mayuri shop

        if hitbox.colliderect(shop) and not shop_destroyed:


            shop_hp -= 1

            kunais.remove(k)


            if shop_hp <= 0:

                shop_hp = 0

                shop_destroyed = True

                explode_shop()



        # Hit biryani

        elif hitbox.colliderect(
            pygame.Rect(790,350,120,80)
        ) and biryani and not biryani_broken:


            biryani_broken = True

            game_over = True

            kunais.remove(k)



        elif k[0] > WIDTH or k[0] < 0:

            kunais.remove(k)




    # Draw Mayuri or explosion

    if not shop_destroyed:


        draw_shop()


    else:


        for p in pieces:


            pygame.draw.rect(
                screen,
                BROWN,
                (p[0],p[1],15,15)
            )


            p[0] += p[2]

            p[1] += p[3]

            p[3] += 0.5



        if len(pieces) > 0:


            if pieces[0][1] > 430:

                biryani = True




    # Draw biryani

    if biryani:

        draw_biryani()



    # Draw Naruto

    draw_ninja(
        player.x,
        player.y
    )


    pygame.display.update()


    clock.tick(60)



pygame.quit()