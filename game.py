from random import randrange
import sys, pygame
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Blazing Fingers")

black = 0,0,0
red = 255,0,0
blue = 0,0,225
white = 255,255,255

size = width, height = 500, 500
screen = pygame.display.set_mode(size)
screen.fill(black)
font = pygame.font.Font(None, 36)

fps = 60
score = 0

randomNum = randrange(1,100)
redRect = 0
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        screen.fill((black))

        pygame.draw.rect(screen, blue, (225,75,50,50))
        pygame.draw.rect(screen, blue, (225,150,50,50))
        pygame.draw.rect(screen, blue, (125,150,50,50))
        pygame.draw.rect(screen, blue, (325,150,50,50))

        if randomNum >=0 and randomNum < 25:
            pygame.draw.rect(screen, red, (225,75,50,50))
            redRect = 1
        if randomNum >= 25 and randomNum < 50:
            pygame.draw.rect(screen, red, (225,150,50,50))
            redRect = 2
        if randomNum >= 50 and randomNum < 75:
            pygame.draw.rect(screen, red, (125,150,50,50))
            redRect = 3
        if randomNum >= 75 and randomNum < 100:
            pygame.draw.rect(screen, red, (325,150,50,50))
            redRect = 4

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    if redRect == 1:
                        randomNum = randrange(1,100)
                        pygame.draw.rect(screen, white, (225,75,50,50))
                        score += 1
                    else:
                        sys.exit()
                if event.key == pygame.K_s:
                    if redRect == 2:
                        randomNum = randrange(1,100)
                        pygame.draw.rect(screen, white, (225,150,50,50))
                        score += 1
                    else:
                        sys.exit()
                if event.key == pygame.K_a:
                    if redRect == 3:
                        randomNum = randrange(1,100)
                        pygame.draw.rect(screen, white, (125,150,50,50))
                        score += 1
                    else:
                        sys.exit()
                if event.key == pygame.K_d:
                    if redRect == 4:
                        randomNum = randrange(1,100)
                        pygame.draw.rect(screen, white, (325,150,50,50))
                        score += 1
                    else:
                        sys.exit()

    showScore = font.render("Score: " + str(score), 1, (255, 255, 255))
    screen.blit(showScore, (100,100))
    pygame.display.flip()
    clock.tick(fps) 
