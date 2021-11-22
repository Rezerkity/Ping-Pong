import pygame
from paddle import Paddle
from ball import ball

pygame.init()

# colours for game
GREEN = 0, 255, 0
RED = 255, 0, 0
BLACK = 0, 0, 0
WHITE = 255, 255, 255

paddleA = Paddle(WHITE, 20, 50)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 20, 50)
paddleB.rect.x = 650
paddleB.rect.y = 200

ball = ball(RED, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

scoreA = 0
scoreB = 0

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

# screen size and stuff
size = 700, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Super Cool Super Secret Chimera Project That Nobody Should See")
carryOn = True
clock = pygame.time.Clock()

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(3)

    if keys[pygame.K_s]:
        paddleA.moveDown(3)

    if keys[pygame.K_UP]:
        paddleB.moveUp(3)

    if keys[pygame.K_DOWN]:
        paddleB.moveDown(3)

    all_sprites_list.update()

    if ball.rect.x >= 680:
        scoreA += 1
        ball.velocity[0] = -ball.velocity[0]

    if ball.rect.x <= 20:
        scoreB += 1
        ball.velocity[0] = -ball.velocity[0]

    if ball.rect.y > 495:
        ball.velocity[1] = -ball.velocity[1]

    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()

    screen.fill(BLACK)

    pygame.draw.line(screen, GREEN, [349, 0], [349, 500], 1)

    all_sprites_list.draw(screen)

    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (250, 10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (420, 10))

    pygame.display.flip()

    clock.tick(60)


pygame.quit()
