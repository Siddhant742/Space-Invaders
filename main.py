import pygame,sys
import random,math
pygame.init()
window = pygame.display.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invaders")

icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

#player
playerX = 370
playerY = 480
playerX_Change = 0
PlayerImg = pygame.image.load('space-invaders.png')
def Player(x,y):
    screen.blit(PlayerImg,(x,y))

#Enemy
# enemyX = random.randint(0,736)
# enemyY = random.randint(50,100)
# enemyX_Change = 0.4
# enemyY_Change = 40 
# EnemyImg = pygame.image.load('enemy.png')
enemyX = []
enemyY = []
enemyX_Change = []
enemyY_Change = []
EnemyImg = []
no_of_Enemies = 6
for i in range(no_of_Enemies):
    EnemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,100))
    enemyX_Change.append(0.4)
    enemyY_Change.append(40)
def Enemy(x,y,i):
    screen.blit(EnemyImg[i],(x,y))

#Bullet
bulletX = 0
bulletY = 480
bulletX_Change = 0
bulletY_Change = 0.7
bullet_State = "ready"
BulletImg = pygame.image.load('bullet.png')   
def FireBullet(x,y):
    global bullet_State
    bullet_State = "fire"
    screen.blit(BulletImg,(bulletX+16,bulletY-24))

#Score    
score_value = 0    
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10
def show_score(x,y):
    score = font.render("Score : "+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

#Collision 
def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2))+(math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False 

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print('key Pressed')
            if event.key == pygame.K_LEFT:
                playerX_Change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_Change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_State is "ready":
                    bulletX = playerX
                    FireBullet(bulletX,bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_Change = 0
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((0,0,0))

    #player movement
    playerX += playerX_Change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736  #64px is the width of the image  
    Player(playerX,playerY)

    #enemy movement
    for i in range(no_of_Enemies):
        if enemyX[i] <= 0:
            enemyX_Change[i] = 0.4
            enemyY[i] += enemyY_Change[i] 
        elif enemyX[i] >= 736:
            enemyX_Change[i] = -0.4 
            enemyY[i] += enemyY_Change[i]  
        enemyX[i] += enemyX_Change[i] 
        Enemy(enemyX[i],enemyY[i],i)

    #bullet movement
    if bulletY <= 0:
        bulletY = 480  
        bullet_State = "ready"
    if bullet_State is "fire":
        bulletY -= bulletY_Change  
        FireBullet(bulletX,bulletY)

    #collision mechanism    
    for i in range(no_of_Enemies):
        if isCollision(enemyX[i],enemyY[i],bulletX,bulletY):
            bulletY = 480
            bullet_State = "ready"
            score_value += 1
            enemyX[i] = random.randint(0,736)
            enemyY[i] = random.randint(50,100)
            
    show_score(textX,textY)    
    pygame.display.update()
