import pygame
import random
import math

# Initialize pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600))

#Background
background = pygame.image.load("background.jpg")

#Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo (1).png")
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load("space-invaders.png")
playerX = 370
playerY = 480
playerX_change = 0


#Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
numOfEnemies = 6

for i in range(numOfEnemies):
    enemyImg.append(pygame.image.load("alien.png")) 
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.3)
    enemyY_change.append(40)

#bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
# bulletX_change = 0
bulletY_change = 0.5
bullet_state = "ready"

score = 0

#Draw the player
def player(x, y):
    screen.blit(playerImg, (x, y))
def enemy(x, y):
    screen.blit(enemyImg, (x, y))
def fire_bullet(z, a):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (z + 16, a + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False
#Game loop
running = True
while running:

    #Set the color
    screen.fill((0, 0, 0))

    #Background image

    screen.blit(background, (0, 0))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #if key stroke is pressed check whether it's right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                    playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3

            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":

                    #Get the current x cord of spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    
    #Checking for boundaries of spaceship
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    #Enemy movement
    for i in range(numOfEnemies):
        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]

    #Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    #Collision
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        enemyX = random.randint(0, 735)
        enemyY = random.randint(50, 150)

    
    player(playerX, playerY)
    enemy(enemyX, enemyY)

    
    pygame.display.update()
