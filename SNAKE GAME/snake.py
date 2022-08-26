import pygame 
import random
pygame.init()
wn = pygame.display.set_mode((500, 400))
l,d,f,end,headx,heady,st=1,2,0,0,[10],[10],1
start=pygame.image.load(r'C:\Users\Bishesh Singh\Desktop\CSE 202\vs code\pyg\sd.jpg')
pause=pygame.image.load(r'C:\Users\Bishesh Singh\Desktop\CSE 202\vs code\pyg\pause.png')
while 1:
    for ev in pygame.event.get():
        if ev==pygame.QUIT:
            break
    wn.fill((0,0,255))
    wn.blit(start,(170,100))
    keys=pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        break
    if keys[pygame.K_ESCAPE]:
        end=1
        break
    pygame.display.update()
while 1:
    pygame.time.delay(80) 
    if end:
        break
    for ev in pygame.event.get():
        if ev==pygame.QUIT:
            break
    keys=pygame.key.get_pressed()
    wn.blit(start,(10,10))
    if keys[pygame.K_END]:
        break
    if keys[pygame.K_LEFT] and d!=2 and d!=0:
        d=1
    if keys[pygame.K_RIGHT] and d!=1 and d!=0:
        d=2
    if keys[pygame.K_UP] and d!=4 and d!=0:
       d=3
    if keys[pygame.K_DOWN] and d!=3 and d!=0:
       d=4
    if keys[pygame.K_BACKSPACE]:
       d=0
    if keys[pygame.K_RETURN]:
        d=4
    if d==1:
        headx[0]-=10
    if d==2:
        headx[0]+=10
    if d==3 :
        heady[0]-=10
    if d==4:
        heady[0]+=10
    wn.fill((255,255,255)) 
    if headx[0]>500 or heady[0]>400 or heady[0]<0 or headx[0]<0:
        end=1
    for i in range(1,l):
        if headx[0]==headx[i] and heady[0]==heady[i]:
            end=1
    if f==0:
        f1=random.randint(0,490)
        f2=random.randint(0,390)
        f=1
    pygame.draw.rect(wn,(0,255,0),(f1,f2,10,11))
    if f1-5<=headx[0]<=f1+5 and f2-5<=heady[0]<=f2+5:
        f=0
        headx.append(headx[l-1])
        heady.append(heady[l-1])
        l+=1
    for i in range(l-1,0,-1):
        headx[i]=headx[i-1]
        heady[i]=heady[i-1]
    for i in range(len(headx)):
        pygame.draw.rect(wn,(255,0,0),(headx[i],heady[i],10,11))
    if d==0:
       wn.blit(pause,(170,110))
    pygame.display.update()
pygame.quit()