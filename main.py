import pygame
import random

pygame.init()

#настройки
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Простая стрельба')
clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
b_color = (255,255,255)

player = pygame.Rect(width//2 - 25, height - 60, 50, 50)
bullets = []
enemies = []

def spawn_enemy():
    enemy = pygame.Rect(random.randint(0, width - 50), -50, 50, 50)
    enemies.append(enemy)

font = pygame.font.Font(None, 74)

running = True
spawn_timer = 0
score = 0
#игрвой цикл
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.right < width:
        player.x += 5
    if keys[pygame.K_SPACE]:
        bullets.append(pygame.Rect(player.centerx - 5, player.top - 10, 10, 20))

    bullets = [b.move(0, -5) for b in bullets if b.bottom > 0]

    if spawn_timer == 0:
        spawn_enemy()
        spawn_timer = 20
    spawn_timer -= 1

    enemies = [e.move(0, 5) for e in enemies if e.bottom < height]

    for bullet in bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                score += 1
                bullets.remove(bullet)
                enemies.remove(enemy)
                break
    screen.fill(black)
    pygame.draw.rect(screen, white, player)
    for bullet in bullets:
        pygame.draw.rect(screen, red, bullet)
    for enemy in enemies:
        pygame.draw.rect(screen, white, enemy)

    score_text = font.render(str(score), True, white)

    screen.blit(score_text, (width // 2, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()