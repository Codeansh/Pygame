def over_show():
    global d
    if d==3:
        d=0
    screen.fill((0,0,0))
    screen.blit(background[d],(0,0))
    over=over_.render('GAME OVER' ,True,(255,255,255))
    over2=over_.render('Restarting....' ,True,(255,0,0))
    screen.blit(over,(350,1000))
    screen.blit(over2,(350,700))
    playerX = 510
    playerY = 1200
    player(playerX,playerY)
    pygame.display.update()
    pygame.time.delay(2000)
   
def show_score(x,y):
    score_=font.render('Score : ' + str(score),True,(255,255,255))
    screen.blit(score_,(x,y))

playerX = 510
playerY = 1200
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
    enemyX_change.append(8.5)
    enemyY_change.append(80)
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