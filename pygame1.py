#pylint:disable=R1703
import pygame
import random
import math
from pygame import mixer
global d 
d=0
pygame.init()
global background
screen = pygame.display.set_mode((1700,1000))
mixer.music.load("background.wav")
mixer.music.play(-1)
pygame.display.set_caption("invaders")
icon = pygame.image.load("logo.png")
background=[]
background.append(pygame.transform.scale(pygame.image.load("level3.png"),(1700,1000)))
background.append(pygame.transform.scale(pygame.image.load("level1.png"),(1700,1000)))
 
background.append(pygame.transform.scale(pygame.image.load("level2.png"),(1700,1000)))
 
playicon = []
playicon.append(pygame.transform.scale(pygame.image.load("p1.png"),(80,80)))


playicon.append(pygame.transform.scale(pygame.image.load("p2.png"),(80,80)))

playicon.append(pygame.transform.scale(pygame.image.load("p3.png"),(80,80)))




bulleticon = pygame.image.load("bullet.png")
bulleticon =pygame.transform.scale(bulleticon,(80,64))
def over_show():
    global d
    if d==3:
        d=0
    screen.fill((0,0,0))
    screen.blit(background[d],(0,0))
    over2=over_.render('GAME OVER' ,True,(255,255,255))
    over=over_.render('Restarting....' ,True,(255,0,0))
    screen.blit(over,(670,600))
    screen.blit(over2,(650,400))
    playerX = 510
    playerY = 1200
    player(playerX,playerY)
    pygame.display.update()
    pygame.time.delay(2000)
   
def show_score(x,y):
    score_=font.render('Score : ' + str(score),True,(255,255,255))
    screen.blit(score_,(x,y))

playerX = 510
playerY = 800
playerX_change=0
playerY_change=0
def player(x,y):
    screen.blit(playicon[d],(x,y)) 
enemyicon=[]
enemyX = []
enemyY = []
enemyX_change=[]
enemyY_change=[]
num_enemy=14
for  i in range(num_enemy):
     
    enemyicon.append(pygame.transform.scale(pygame.image.load("ufo1.png"),(80,80)))
    enemyX.append(random.randint(10,990))
    enemyY.append(random.randint(10,200))
    enemyX_change.append(2.5)
    enemyY_change.append(40)
def enemy(x,y,i):
    
    screen.blit(enemyicon[i],(x,y)) 
    
bulletX = 0
bulletY = 0
bulletX_change=0
bulletY_change=20
bullet_state='ready'

def fire_bullet(x,y):
    global bullet_state
    bullet_state='fire'
    screen.blit(bulleticon,(x,y-60))
def iscollision(enX,enY,bx,by):
    distance=math.sqrt((math.pow((enX-bx),2))+(math.pow((enY-by),2)))
    if distance<=45:
        return True
    else:
        return False
#f=open('score.txt','w')
score=0
#f.write('+0')
font =pygame.font.Font('freesansbold.ttf',42)
testX =10
testY=10

over_=pygame.font.Font('freesansbold.ttf',64)

    
pygame.display.set_icon(icon)
running = True
#f=open('output.txt','w')
#f.write('\n')
while running :
    playerX +=0
    playerY-=0
    screen.fill((0,0,0))
    screen.blit(background[d],(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False
        
        if event.type==pygame.KEYDOWN:
           # f=open('output.txt','a')
        #    f.write('Some key is Pressed\n')
            
            if event.key==pygame.K_LEFT:
                playerX_change=-7.5
                playerY_change=0
                # f=open('output.txt','a')
                # f.write('LEFT Pressed\n')
                
                print("left pressed\n")
            if event.key==pygame.K_RIGHT:
                playerX_change=7.5
                playerY_change=0
                # f=open('output.txt','a')
                # f.write('RIGHT Pressed\n')
                # print("right pressed")
                
            if event.key==pygame.K_UP:
                playerY_change=-2.5
                playerX_change=0
                
            if event.key==pygame.K_DOWN:
                playerY_change=2.5
                playerX_change=0
                
            if event.key == pygame.K_s:
                playerX_change=0
                playerY_change=0
            if event.key==pygame.K_SPACE:
              if bullet_state =='ready':
                  bulletX=playerX
                  bullet_sound=mixer.Sound('laser.wav')
                  bullet_sound.play()
                  fire_bullet(bulletX,bulletY+playerY)
              
        if event.type ==pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                 playerX_change=0
                 playerY_change=0
                
               
                # f=open('output.txt','a')
                # f.write('Released\n')
                # print("key released")
    playerX+=playerX_change
    playerY+=playerY_change
    
    if playerX<=0:
        playerX=0
    elif playerX>=1600:
        playerX=1600
        
    
   
    
    for i in range(num_enemy):
       
        if enemyY[i] >=playerY-100 :
           d+=1
           for j in range(num_enemy):
               enemyY[j] =0
             
           playerX = 510
           playerY = 800
           bulletX=playerX
           bulletY=0
           bullet_state ='ready'
     
           over_show()
           break
        enemyX[i]+=enemyX_change[i]
        
        if enemyX[i]<=0:
            enemyX_change[i]=2.5
            enemyY[i]+=enemyY_change[i]
        elif enemyX[i]>=1600:
            enemyX_change[i]=-2.5
            enemyY[i]+=enemyY_change[i]
        bulY=bulletY+playerY
        coll =iscollision(enemyX[i],enemyY[i],bulletX,bulY)
        if coll:
            coll_sound=mixer.Sound('explosion.wav')
            coll_sound.play()
            bullet_state='ready'
            bulletY=0
            score+=1
            f=open('score.txt','a')
            f.write('+1')
            enemyX[i] = random.randint(0,990)
            enemyY[i] = random.randint(40,200)
        enemy(enemyX[i],enemyY[i],i)
            
    if bulletY+playerY<=0:
        bulletY=0
        bullet_state='ready'
        
      
    if bullet_state == 'fire':
        fire_bullet(bulletX,bulletY+playerY)
        bulletY-=bulletY_change
    
    player(playerX,playerY)
    show_score(testX,testY)
     
    pygame.display.update()
