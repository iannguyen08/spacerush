import pygame,random,sys,math
pygame.init()
pygame.display.set_caption("S P A C E  R U S H")

width=530
height=900
buffer=30
screen=pygame.display.set_mode((width,height))
clock=pygame.time.Clock()

def displaytime():
    time=int(pygame.time.get_ticks()/1000)-starttime
    timesurf=font.render(str(time),True,"White")
    timerect=timesurf.get_rect(center=(width/2,150))
    screen.blit(timesurf,timerect)
starttime=0
on=True

rocketimg=pygame.image.load("rocket-ship.png")
rocket=pygame.transform.scale(rocketimg,(162,250))
rocketx=width/2
rockety=700
rocketrect=pygame.Rect(rocketx,rockety,150,250)
rocketv=0
rocketa=1
rocketd=.1
maxspeed=10

asteroidimg=pygame.image.load("asteroid.png")
asteroid=pygame.transform.scale(asteroidimg,(200,200))
asteroidx=random.randint(buffer,width-buffer)
asteroidx2=random.randint(buffer,width-buffer)
asteroidy=-300
asteroidy2=-900
asteroidrect=pygame.Rect(asteroidx,asteroidy,130,130)
asteroidrect2=pygame.Rect(asteroidx,asteroidy,130,130)

backgroundimg=pygame.image.load("background.png")
backgroundrect=backgroundimg.get_rect(center=(width/2,height/2))
backgroundrect2=backgroundimg.get_rect(center=(width/2,height/2-height))

font=pygame.font.SysFont("segoeuisemibold",50)
smallfont=pygame.font.SysFont("segoeuisemibold",20)
smallfont2=pygame.font.SysFont("segoeuisemibold",13)
end=font.render("G A M E  O V E R",True, "White")
endrect=end.get_rect(center=(width/2,height/2))

def displayinstructions():
    instructions=smallfont.render("press SPACE to start",True,"White")
    instructionsrect=instructions.get_rect(center=(width/2,height-400))
    screen.blit(instructions,instructionsrect)   
def introscreen():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                return False
        
        screen.blit(backgroundimg,backgroundrect)
        screen.blit(backgroundimg,backgroundrect2)
        backgroundrect.y+=10
        backgroundrect2.y+=10
        if backgroundrect.y>900:
            backgroundrect.y=0
        if backgroundrect2.y>0:
            backgroundrect2.y=-900
        
        title=font.render("S P A C E  R U S H",True,"White")
        titlerect=title.get_rect(center=(width/2,height/2))
        screen.blit(title,titlerect)
        
        displayinstructions()
        
        instructions2=smallfont2.render("use arrow keys to play",True,"White")
        instructionsrect2=instructions2.get_rect(center=(width/2,850))
        screen.blit(instructions2,instructionsrect2)
        
        pygame.display.update()
        clock.tick(60)
introscreen()      

starttime=int(pygame.time.get_ticks()/1000)
bouncetime=0

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                on=True
                asteroidx=random.randint(buffer,width-buffer)
                asteroidx2=random.randint(buffer,width-buffer)
                asteroidy=-300
                asteroidy2=-900
                rocketx=width/2
                rockety=height-200
                rocketv=0
                starttime=int(pygame.time.get_ticks()/1000)
    input=pygame.key.get_pressed()  
    if input[pygame.K_a]or input[pygame.K_LEFT]:
        rocketv-=rocketa
    if input[pygame.K_d]or input[pygame.K_RIGHT]:
        rocketv+=rocketa
    if rocketv>maxspeed:
        rocketv=maxspeed
    if rocketv<-maxspeed:
        rocketv=-maxspeed
    if not input[pygame.K_a] and not input[pygame.K_d] and not input[pygame.K_LEFT] and not input[pygame.K_RIGHT]:
        if rocketv>0:
            rocketv-=rocketd
        if rocketv<0:
            rocketv+=rocketd
    rocketx+=rocketv
    bouncetime+=.1
    rockety=700+25*math.sin(bouncetime)
    
    if on:
        asteroidy+=10
        asteroidy2+=10
        rocketrect.center=(rocketx,rockety)
        asteroidrect.center=(asteroidx,asteroidy)
        asteroidrect2.center=(asteroidx2,asteroidy2)
        
        if asteroidy==1100:
            asteroidy=-300
            asteroidx=random.randint(buffer,width-buffer)
        if asteroidy2==1100:
            asteroidy2=-300
            asteroidx2=random.randint(buffer,width-buffer)
        screen.blit(backgroundimg,backgroundrect)
        screen.blit(backgroundimg,backgroundrect2)
        backgroundrect.y+=30
        if backgroundrect.y>900:
            backgroundrect.y=0
        backgroundrect2.y+=30
        if backgroundrect2.y>0:
            backgroundrect2.y=-900
        screen.blit(rocket,rocketrect)
        screen.blit(asteroid,asteroidrect)
        screen.blit(asteroid,asteroidrect2)
        displaytime()
    if rocketrect.colliderect(asteroidrect) or rocketrect.colliderect(asteroidrect2):
        on=False
        screen.blit(end,endrect)
        displayinstructions()
    if rocketx<0:
        rocketx=0
    if rocketx>width:
        rocketx=width
    score=smallfont.render("S C O R E",True,"White")
    scorerect=score.get_rect(center=(width/2,100))
    screen.blit(score,scorerect)
    pygame.display.update()
    clock.tick(60)
    
        

    
    
