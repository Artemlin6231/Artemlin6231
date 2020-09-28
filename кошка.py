import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((395, 560))
#рисуем верх
rect(screen, (165, 42, 42), (0,0, 395, 255))
rect(screen, (127, 255, 212), (215,15, 175, 235))
a=230
for i in range(2):
    rect(screen, (0,0,255), (a,25, 70, 55))
    rect(screen, (0,0,255), (a,90, 70, 140))
    a+=80
#рисуем низ
rect(screen, (100,40,0), (0,255, 396, 305))
line(screen,(0,0,0),(150,520),(260,520),1)
circle(screen, (43, 43, 43), (240, 500), 30)
b=480
for i in range(3):
    line(screen,(0,0,0),(220,b),(260,b+25),1)
    b+=5
#NewSurface= pygame.transform.rotate(screen,90)
#NewSurface1= pygame.transform.rotate(screen,60)


#рисуем cat
ellipse(screen,(255, 130, 171),(250,300,150,60))
ellipse(screen,(0,0,0),(250,300,150,60),1)

ellipse(screen,(255, 130, 171),(50,265,260,140))
ellipse(screen,(0,0,0),(50,265,260,140),1)

#ellipse(NewSurface,(255, 130, 171),(36,320,74,40))
#ellipse(NewSurface,(0,0,0),(36,320,74,40),1)

ellipse(screen,(255, 130, 171),(34,330,31,50))
ellipse(screen,(0,0,0),(34,330,31,50),1)

ellipse(screen,(255, 130, 171),(56,370,74,40))
ellipse(screen,(0,0,0),(56,370,74,40),1)

ellipse(screen,(255, 130, 171),(56,370,74,40))
ellipse(screen,(0,0,0),(56,370,74,40),1)
ellipse(screen,(255, 130, 171),(10,275,100,90))
ellipse(screen,(0,0,0),(10,275,100,90),1)


circle(screen, (255, 130, 171), (270,370), 45)
circle(screen, (0,0,0), (270,370), 45,1)

ellipse(screen,(255, 130, 171),(280,380,35,65))
ellipse(screen,(0,0,0),(280,380,35,65),1)



#ears and eyes
polygon(screen, (255, 130, 171), [(85,285), (110,270),
                               (105,305)])
polygon(screen, (0,0,0), [(85,285), (110,270),
                               (105,305)],1)
polygon(screen, (255,100,180), [(90,285), (105,275),
                               (105,300)])
polygon(screen, (0,0,0), [(90,285), (105,275),
                               (105,300)],1)

polygon(screen, (255, 130, 171), [(8,273), (17,305),
                               (35,287)])
polygon(screen, (0,0,0), [(8,273), (17,305),
                               (35,287)],1)
polygon(screen, (255,100,180), [(11,278), (18,300),
                               (30,286)])
polygon(screen, (0,0,0), [(11,278), (18,300),
                               (30,286)],1)
x=34
for i in range(2):
    ellipse(screen, (0,255,170), (x,305,20,25))
    ellipse(screen, (0, 0, 0), (x,305,20,25), 1)
    ellipse(screen, (0, 0, 0), (x+10, 306, 5, 20), 0)
    x+=46
polygon(screen, (255,100,180), [(61,340), (69,340),
                               (65,345)])
polygon(screen, (0,0,0), [(61,340), (69,340),
                               (65,345)],1)
line(screen,(0,0,0),(65,345),(65,350),1)

#усы
line(screen,(0,0,0),(75,345),(120,340),1)
line(screen,(0,0,0),(75,348),(120,348),1)
line(screen,(0,0,0),(75,351),(120,356),1)
line(screen,(0,0,0),(55,345),(30,340),1)
line(screen,(0,0,0),(55,348),(30,348),1)
line(screen,(0,0,0),(55,351),(30,356),1)









pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
