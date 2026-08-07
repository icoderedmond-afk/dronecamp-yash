
import pygame
import random
import sys

pygame.init()

# =========================
# SETTINGS
# =========================

WIDTH = 500
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()

# =========================
# COLORS
# =========================

SKY = (90, 200, 255)
GREEN = (50, 190, 70)
DARK_GREEN = (30, 140, 50)
YELLOW = (255, 220, 0)
ORANGE = (255, 150, 0)
WHITE = (255, 255, 255)
BLACK = (20, 20, 20)

# =========================
# FONTS
# =========================

title_font = pygame.font.Font(None, 80)
font = pygame.font.Font(None, 45)
small_font = pygame.font.Font(None, 32)

# =========================
# HIGH SCORE
# =========================

HIGH_SCORE_FILE = "flappy_highscore.txt"


def load_high_score():
    try:
        with open(HIGH_SCORE_FILE, "r") as file:
            return int(file.read())
    except:
        return 0


def save_high_score(score):
    with open(HIGH_SCORE_FILE, "w") as file:
        file.write(str(score))


high_score = load_high_score()

# =========================
# BUTTON CLASS
# =========================

class Button:

    def __init__(self, text, x, y, width, height):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):

        mouse = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse):
            color = DARK_GREEN
        else:
            color = GREEN

        pygame.draw.rect(
            screen,
            color,
            self.rect,
            border_radius=15
        )

        pygame.draw.rect(
            screen,
            WHITE,
            self.rect,
            3,
            border_radius=15
        )

        text_surface = font.render(
            self.text,
            True,
            WHITE
        )

        screen.blit(
            text_surface,
            (
                self.rect.centerx - text_surface.get_width() // 2,
                self.rect.centery - text_surface.get_height() // 2
            )
        )

    def clicked(self, position):
        return self.rect.collidepoint(position)


# =========================
# BUTTONS
# =========================

start_button = Button(
    "START GAME",
    125,
    300,
    250,
    70
)

exit_button = Button(
    "EXIT",
    125,
    400,
    250,
    70
)

# =========================
# GAME VARIABLES
# =========================

bird_x = 100
bird_y = 350
bird_size = 20
bird_velocity = 0

gravity = 0.5
flap_power = -9

pipes = []

pipe_width = 70
pipe_gap = 180
pipe_speed = 4

score = 0

game_started = False
game_over = False


# =========================
# CREATE PIPE
# =========================

def create_pipe():

    top_height = random.randint(100, 400)

    pipes.append({
        "x": WIDTH,
        "top": top_height,
        "bottom": top_height + pipe_gap,
        "passed": False
    })


# =========================
# RESET GAME
# =========================

def reset_game():

    global bird_y
    global bird_velocity
    global pipes
    global score
    global game_over

    bird_y = 350
    bird_velocity = 0

    pipes = []

    score = 0

    game_over = False

    create_pipe()


# =========================
# MAIN LOOP
# =========================

running = True

while running:

    mouse_clicked = False
    mouse_position = None

    # =========================
    # EVENTS
    # =========================

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # -------------------------
        # MOUSE
        # -------------------------

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                mouse_clicked = True
                mouse_position = event.pos

        # -------------------------
        # KEYBOARD
        # -------------------------

        if event.type == pygame.KEYDOWN:

            # ESC = EXIT
            if event.key == pygame.K_ESCAPE:
                running = False

            # SPACE
            if event.key == pygame.K_SPACE:

                # GAME OVER = RESTART
                if game_started and game_over:

                    reset_game()

                # PLAYING = FLAP
                elif game_started:

                    bird_velocity = flap_power

    # =========================================================
    # MENU
    # =========================================================

    if not game_started:

        screen.fill(SKY)

        # Title
        title = title_font.render(
            "FLAPPY BIRD",
            True,
            WHITE
        )

        screen.blit(
            title,
            (
                WIDTH // 2 - title.get_width() // 2,
                100
            )
        )

        # Decorative bird
        pygame.draw.circle(
            screen,
            YELLOW,
            (WIDTH // 2, 210),
            30
        )

        pygame.draw.circle(
            screen,
            WHITE,
            (WIDTH // 2 + 10, 200),
            8
        )

        pygame.draw.circle(
            screen,
            BLACK,
            (WIDTH // 2 + 12, 200),
            4
        )

        # Start button
        start_button.draw()

        # Exit button
        exit_button.draw()

        # High score
        high_text = small_font.render(
            "High Score: " + str(high_score),
            True,
            WHITE
        )

        screen.blit(
            high_text,
            (
                WIDTH // 2 - high_text.get_width() // 2,
                510
            )
        )

        # Menu clicks
        if mouse_clicked:

            if start_button.clicked(mouse_position):

                reset_game()
                game_started = True

            elif exit_button.clicked(mouse_position):

                running = False

    # =========================================================
    # GAME
    # =========================================================

    else:

        # -------------------------
        # CLICK
        # -------------------------

        if mouse_clicked:

            # Click after game over = restart
            if game_over:

                reset_game()

            # Normal click = flap
            else:

                bird_velocity = flap_power

        # -------------------------
        # UPDATE
        # -------------------------

        if not game_over:

            # Bird physics
            bird_velocity += gravity
            bird_y += bird_velocity

            # Move pipes
            for pipe in pipes:

                pipe["x"] -= pipe_speed

                # Score
                if (
                    not pipe["passed"]
                    and pipe["x"] + pipe_width < bird_x
                ):

                    pipe["passed"] = True

                    score += 1

                    # New high score
                    if score > high_score:

                        high_score = score
                        save_high_score(high_score)

            # Create new pipes
            if len(pipes) == 0 or pipes[-1]["x"] < 250:

                create_pipe()

            # Remove old pipes
            pipes = [
                pipe for pipe in pipes
                if pipe["x"] + pipe_width > 0
            ]

            # Bird rectangle
            bird_rect = pygame.Rect(
                bird_x - bird_size,
                bird_y - bird_size,
                bird_size * 2,
                bird_size * 2
            )

            # -------------------------
            # PIPE COLLISION
            # -------------------------

            for pipe in pipes:

                top_pipe = pygame.Rect(
                    pipe["x"],
                    0,
                    pipe_width,
                    pipe["top"]
                )

                bottom_pipe = pygame.Rect(
                    pipe["x"],
                    pipe["bottom"],
                    pipe_width,
                    HEIGHT
                )

                if bird_rect.colliderect(top_pipe):
                    game_over = True

                if bird_rect.colliderect(bottom_pipe):
                    game_over = True

            # -------------------------
            # CEILING
            # -------------------------

            if bird_y - bird_size <= 0:

                game_over = True

            # -------------------------
            # GROUND
            # -------------------------

            if bird_y + bird_size >= HEIGHT:

                game_over = True

        # =====================================================
        # DRAW GAME
        # =====================================================

        screen.fill(SKY)

        # -------------------------
        # PIPES
        # -------------------------

        for pipe in pipes:

            # Top pipe
            pygame.draw.rect(
                screen,
                GREEN,
                (
                    pipe["x"],
                    0,
                    pipe_width,
                    pipe["top"]
                )
            )

            # Bottom pipe
            pygame.draw.rect(
                screen,
                GREEN,
                (
                    pipe["x"],
                    pipe["bottom"],
                    pipe_width,
                    HEIGHT
                )
            )

            # Top pipe cap
            pygame.draw.rect(
                screen,
                DARK_GREEN,
                (
                    pipe["x"] - 5,
                    pipe["top"] - 20,
                    pipe_width + 10,
                    20
                )
            )

            # Bottom pipe cap
            pygame.draw.rect(
                screen,
                DARK_GREEN,
                (
                    pipe["x"] - 5,
                    pipe["bottom"],
                    pipe_width + 10,
                    20
                )
            )

        # -------------------------
        # BIRD
        # -------------------------

        pygame.draw.circle(
            screen,
            YELLOW,
            (
                bird_x,
                int(bird_y)
            ),
            bird_size
        )

        # Eye
        pygame.draw.circle(
            screen,
            WHITE,
            (
                bird_x + 7,
                int(bird_y) - 7
            ),
            7
        )

        pygame.draw.circle(
            screen,
            BLACK,
            (
                bird_x + 9,
                int(bird_y) - 7
            ),
            3
        )

        # Beak
        pygame.draw.polygon(
            screen,
            ORANGE,
            [
                (bird_x + 15, int(bird_y)),
                (bird_x + 35, int(bird_y) + 7),
                (bird_x + 15, int(bird_y) + 13)
            ]
        )

        # -------------------------
        # SCORE
        # -------------------------

        score_text = font.render(
            str(score),
            True,
            WHITE
        )

        screen.blit(
            score_text,
            (
                WIDTH // 2 - score_text.get_width() // 2,
                30
            )
        )

        # =====================================================
        # GAME OVER
        # =====================================================

        if game_over:

            # Dark overlay
            overlay = pygame.Surface(
                (WIDTH, HEIGHT)
            )

            overlay.set_alpha(160)
            overlay.fill(BLACK)

            screen.blit(
                overlay,
                (0, 0)
            )

            # Game over text
            game_over_text = title_font.render(
                "GAME OVER",
                True,
                WHITE
            )

            screen.blit(
                game_over_text,
                (
                    WIDTH // 2
                    - game_over_text.get_width() // 2,
                    220
                )
            )

            # Score
            score_text = font.render(
                "Score: " + str(score),
                True,
                WHITE
            )

            screen.blit(
                score_text,
                (
                    WIDTH // 2
                    - score_text.get_width() // 2,
                    320
                )
            )

            # High score
            high_text = small_font.render(
                "High Score: " + str(high_score),
                True,
                WHITE
            )

            screen.blit(
                high_text,
                (
                    WIDTH // 2
                    - high_text.get_width() // 2,
                    370
                )
            )

            # Restart instructions
            restart_text = small_font.render(
                "SPACE or CLICK to restart",
                True,
                WHITE
            )

            screen.blit(
                restart_text,
                (
                    WIDTH // 2
                    - restart_text.get_width() // 2,
                    450
                )
            )

    # =========================
    # UPDATE SCREEN
    # =========================

    pygame.display.flip()

    clock.tick(60)


pygame.quit()
sys.exit()

