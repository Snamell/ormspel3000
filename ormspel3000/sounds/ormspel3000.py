import pygame
import random


pygame.init()

pygame.mixer.init()
background_music_file = "sounds/gamingmuskk.mp3"
pygame.mixer.music.load(background_music_file)
pygame.mixer.music.play(-1)


walking_sound = "sounds/squidward.mp3"
walking = pygame.mixer.Sound(walking_sound)
channel1 = pygame.mixer.Channel(0)


collect_sound = "sounds/Nyah.mp3"
collect = pygame.mixer.Sound(collect_sound)
channel2 = pygame.mixer.Channel(0)


collide_sound = "sounds/Yamete.mp3"
collide = pygame.mixer.Sound(collide_sound)
channel3 = pygame.mixer.Channel(0)


direction = ""


enemy_health = 100


WIDTH, HEIGHT = 640, 480
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ormspel3000 (2D-Game)")

background_image = pygame.image.load("rainbowbridge.png")
background_image = pygame.transform.scale(background_image, (640, 480))
background_image_rect = background_image.get_rect()
background_image_rect.x = 0
background_image_rect.y = 0


BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
PINK = (159, 43, 104)

player_color = GREEN

font_title = pygame.font.SysFont(None, 48)
font_button = pygame.font.SysFont(None, 32)


clock = pygame.time.Clock()


game_state = "menu"


snake_size = 20
snake_x = 300
snake_y = 300

player_image_index = 0

player_image_file1 = "orm/thwok.jpg"
player_image_file2 = "orm/snortcoke.jpg"
player_images = [pygame.image.load(player_image_file1), pygame.image.load(player_image_file2)]
player_image = pygame.transform.scale(player_images[player_image_index], (snake_size, snake_size))


fruit_image_index = 0

fruit_image_file1 = "fruits/appel.png"
fruit_image_file2 = "fruits/banan.png"
current_image = fruit_image_file1
fruit_images = [pygame.image.load(fruit_image_file1), pygame.image.load(fruit_image_file2)]
fruit_image = pygame.transform.scale(fruit_images[fruit_image_index], (snake_size, snake_size))


enemy1 = pygame.image.load("enemy.png")
enemy1 = pygame.transform.scale(enemy1, (20, 20))
getoutofmyhead = enemy1.get_rect()
getoutofmyhead.x = 0
getoutofmyhead.y = 480


bullet_list = []

bullet_speed = 5


velocity_x = 0
velocity_y = 0


food_x = random.randint(0, WIDTH - snake_size) // snake_size * snake_size
food_y = random.randint(0, HEIGHT - snake_size) // snake_size * snake_size


score = 0

snake_body = []
snake_length = 1
movement_multiplier = 1


while True:

    win.blit(background_image, background_image_rect)

    win.blit(enemy1, getoutofmyhead)

    if game_state == "menu":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_state = "running"

        win.fill(BLACK)
        title_text = font_title.render("Snake Game", True, WHITE)
        start_text = font_button.render("Press ENTER to start", True, GRAY)
        win.blit(
            title_text,
            (
                WIDTH // 2 - title_text.get_width() // 2,
                HEIGHT // 2 - title_text.get_height(),
            ),
        )
        win.blit(
            start_text,
            (
                WIDTH // 2 - start_text.get_width() // 2,
                HEIGHT // 2 + title_text.get_height(),
            ),
        )

    elif game_state == "running":

        if snake_x >= getoutofmyhead.x:
            getoutofmyhead.x += 2
        if snake_x <= getoutofmyhead.x:
            getoutofmyhead.x -= 2
        if snake_y >= getoutofmyhead.y:
            getoutofmyhead.y += 2
        if snake_y <= getoutofmyhead.y:
            getoutofmyhead.y -= 2
        
        for i in snake_body:
            if getoutofmyhead.collidepoint((i[0], i[1])):
                collide.play()
                game_state = "game_over"


        if score >= 5:
            bullet_speed += 5
        
        elif score >=10:
            bullet_speed += 5

        elif score >=15:
            bullet_speed += 5

        elif score >=20:
            bullet_speed += 5

        elif score >=25:
            bullet_speed += 10


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and velocity_y != snake_size:
                    velocity_x = 0
                    velocity_y = -snake_size * movement_multiplier
                    player_image_index = (player_image_index + 1) % len(player_images)
                if not channel1.get_busy():
                        walking.play()

                elif event.key == pygame.K_s and velocity_y != -snake_size:
                    velocity_x = 0
                    velocity_y = snake_size * movement_multiplier
                    player_image_index = (player_image_index + 1) % len(player_images)
                if not channel1.get_busy():
                        walking.play()

                elif event.key == pygame.K_a and velocity_x != snake_size:
                    velocity_x = -snake_size * movement_multiplier
                    velocity_y = 0
                    player_image_index = (player_image_index + 1) % len(player_images)
                if not channel1.get_busy():
                        walking.play()

                elif event.key == pygame.K_d and velocity_x != -snake_size:
                    velocity_x = snake_size * movement_multiplier
                    velocity_y = 0
                    player_image_index = (player_image_index + 1) % len(player_images)
                if not channel1.get_busy():
                        walking.play()

                elif event.key == pygame.K_SPACE:
                    bullet = pygame.image.load("bulletqueen.png")
                    bullet = pygame.transform.scale(bullet, (16, 16))
                    bulletqueen = bullet.get_rect()
                    bulletqueen.x = snake_x
                    bulletqueen.y = snake_y
                    bullet_list.append([bullet, bulletqueen, direction])
                    

                if event.key == pygame.K_w:
                    direction = "up"
                elif event.key == pygame.K_s:
                    direction = "down"
                elif event.key == pygame.K_a:
                    direction = "left"
                elif event.key == pygame.K_d:
                    direction = "right"

            for i in bullet_list:
                win.blit(i[0], i[1])
                if i[2] == "up":
                    i[1].y -= 20
                elif i[2] == "down":
                    i[1].y += 20
                elif i[2] == "right":
                    i[1].x += 20
                elif i[2] == "left":
                    i[1].x -= 20
                
                if i[1].x >= 640 or i[1].x <= 0 or i[1].y >= 480 or i[1].y <= 0:
                    bullet_list.remove(i)

            
            for i in bullet_list:
                if getoutofmyhead.colliderect(i[1]):
                    enemy_health -= 20                    
                    if enemy_health <= 0:
                        getoutofmyhead.x = random_enemy_x
                        getoutofmyhead.y = random_enemy_y
                        enemy_health = 100
            

        enemy_spawn_coordinates_x = [0, 640]
        enemy_spawn_coordinates_y = [0, 480]

        rand_enemy_x = random.randint(0, len(enemy_spawn_coordinates_x)-1)
        rand_enemy_y = random.randint(0, len(enemy_spawn_coordinates_y)-1)

        random_enemy_x = enemy_spawn_coordinates_x[rand_enemy_x]
        random_enemy_y = enemy_spawn_coordinates_y[rand_enemy_y]


        snake_x += velocity_x
        snake_y += velocity_y

        if snake_x == food_x and snake_y == food_y:
            food_x = random.randint(0, WIDTH - snake_size) // snake_size * snake_size
            food_y = random.randint(0, HEIGHT - snake_size) // snake_size * snake_size
            score += 1
            snake_length += 1
            fruit_image_index = (fruit_image_index + 1) % len(fruit_images)
            if not channel2.get_busy():
                collect.play()

        if (
            snake_x < 0
            or snake_x >= WIDTH
            or snake_y < 0
            or snake_y >= HEIGHT
            or [snake_x, snake_y] in snake_body[1:]
        ):
            game_state = "game_over"


        snake_body.append([snake_x, snake_y])
        if len(snake_body) > snake_length:
            del snake_body[0]
        
        player_image = pygame.transform.scale(player_images[player_image_index], (snake_size, snake_size))
        fruit_image = pygame.transform.scale(fruit_images[fruit_image_index], (snake_size, snake_size))

        for body_part in snake_body:
            win.blit(player_image, (body_part[0], body_part[1]))

        win.blit(fruit_image, (food_x, food_y))

        score_text = font_button.render("Score: " + str(score), True, WHITE)
        win.blit(score_text, (10, 10))

    elif game_state == "game_over":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_state = "running"
                    snake_x = 300
                    snake_y = 300
                    velocity_x = 0
                    velocity_y = 0
                    score = 0
                    food_x = (
                        random.randint(0, WIDTH - snake_size) // snake_size * snake_size
                    )
                    food_y = (
                        random.randint(0, HEIGHT - snake_size)
                        // snake_size
                        * snake_size
                    )
                    snake_body = []
                    snake_length = 1
                elif event.key == pygame.K_q:
                    pygame.quit()
                    exit()

        win.fill(BLACK)
        game_over_text = font_title.render("Game Over", True, WHITE)
        score_text = font_button.render("Score: " + str(score), True, WHITE)
        restart_text = font_button.render("Press ENTER to restart", True, GRAY)
        quit_text = font_button.render("Press Q to quit", True, GRAY)
        win.blit(
            game_over_text,
            (
                WIDTH // 2 - game_over_text.get_width() // 2,
                HEIGHT // 2 - game_over_text.get_height(),
            ),
        )
        win.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
        win.blit(
            restart_text,
            (
                WIDTH // 2 - restart_text.get_width() // 2,
                HEIGHT // 2 + game_over_text.get_height(),
            ),
        )
        win.blit(
            quit_text,
            (
                WIDTH // 2 - quit_text.get_width() // 2,
                HEIGHT // 2 + game_over_text.get_height() + restart_text.get_height(),
            ),
        )

    pygame.display.update()

    clock.tick(12)
