import pygame
import random
pygame.init()
wn = pygame.display.set_mode((800, 600))
x,y,x1,y1=10,450,30,-100
n=0
i=y
a=x
m=-300
m1=180
point=0
t,t1=0,-100
bak=pygame.image.load(r'C:\Users\Bishesh Singh\Desktop\CSE 202\vs code\pyg\bg.png')
image = pygame.image.load(r'C:\Users\Bishesh Singh\Desktop\CSE 202\vs code\pyg\clas1.gif')
las=pygame.image.load(r'C:\Users\Bishesh Singh\Desktop\CSE 202\vs code\pyg\laser.jpg')
ene=pygame.image.load(r'C:\Users\Bishesh Singh\Desktop\CSE 202\vs code\pyg\opp.gif')
blast=pygame.image.load(r'C:\Users\Bishesh Singh\Desktop\CSE 202\vs code\pyg\blast.gif')

while True:
    pygame.time.delay(50) 
    for ev in pygame.event.get():
        if ev==pygame.QUIT:
            break
    keys=pygame.key.get_pressed()
    if x==a or i==y:
            a=x
    if keys[pygame.K_LEFT] and x>=0:
        x-=30
    elif keys[pygame.K_RIGHT] and x<=650:
        x+=30
    elif keys[pygame.K_END] or m1<=0:
        break
    wn.fill((0,0,0))
    wn.blit(bak, (0,m))
    wn.blit(image, (x,y)) 
    wn.blit(ene, (x1,y1))
    pygame.draw.rect(wn,(255,0,0),(10,30,180,15))
    pygame.draw.rect(wn,(0,255,0),(10,30,m1,15))
    font1 = pygame.font.SysFont('POINTS : '+str(point), 40)
    img1 = font1.render('POINTS : '+str(point), True, (255,255,255))
    wn.blit(img1, (600,10))
    font1 = pygame.font.SysFont('HEALTH', 20)
    img2 = font1.render('HEALTH', True, (255,255,255))
    wn.blit(img2, (10,10))
    y1+=4
    m+=2
    wn.blit(las, (x1+50,t1))
    t1+=30 
    if t1>=800:
        t1=y1+100

    if x-60<=x1<=x+60 and y+10<=t1<=y+100:
        wn.blit(blast,(x,y))
        wn.blit(blast,(x,y))
        m1-=10
        t1=y1+80
    
    if y1==800:
        y1=-100
        x1=random.randint(0,650)

    if m==0:
        m=-300
    if keys[pygame.K_0] or n==1:
        n=1
        i=i-30
        wn.blit(las, (a+41,i)) 
        wn.blit(las, (a+81,i))
        if i<=0 :
            n=0
            i=y
        if  (x1-60<=a<=x1+60 and y1-30<=i<=y1+100):
            n=0
            i=y
            point+=30
            wn.blit(blast,(x1,y1))
            y1=-100
            x1=random.randint(0,650)
    if x-40<=x1<=x+40 and y-30<=y1<=y+100:
        y1=-100
        x1=random.randint(0,650)
        wn.blit(blast,(x,y))
        m1-=45
    pygame.display.update()
pygame.quit()