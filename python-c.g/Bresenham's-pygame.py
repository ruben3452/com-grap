import sys,pygame
from pygame import gfxdraw
 
pygame.init()
screen = pygame.display.set_mode((400,400))
screen.fill((0,0,0))
pygame.display.flip()
white = (255,255,255)
 
def bresenham(x1,y1,x2,y2):
    dx = x2-x1
    dy = y2-y1
 
    D = 2*dy - dx
    gfxdraw.pixel(screen,x1,y1,white)
    y = y1
 
    for x in range(x1+1,x2+1):
        if D > 0:
            y += 1
            gfxdraw.pixel(screen,x,y,white)
            
            D += (2*dy-2*dx)
        else:
            gfxdraw.pixel(screen,x,y,white)
            D += 2*dy
    pygame.display.flip()
 
bresenham(20,20,60,60)
 
while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
       pygame.quit()
