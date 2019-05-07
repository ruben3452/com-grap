import sys,math,pygame,ImageDraw
from pygame.locals import *

color=0,0,0
azul=(0,0,255)
morado = (199,21,133)
tamano= ancho, alto=500,500
pantalla=pygame.display.set_mode(tamano)
pantalla.fill(color)

def poligonos(x,y,r,n):

    a=(math.pi/2)-(math.pi/n)
    x1=int(x-r*math.cos(a))
    y1=int(y+r*math.sin(a))
    j1=(x-r*math.cos(a))
    k1=(y+r*math.sin(a))
    
    for i in range (1,n+1):
        a=a+2*math.pi/n
        x2=int(x-r*math.cos(a))
        y2=int(y+r*math.sin(a))
        pantalla.set_at((x1,y1), azul)
        pantalla.set_at((x2,y2), azul)
        pygame.draw.line(pantalla,azul,(x1, y1),(x2, y2),5)     
        x1=x2
        y1=y2
        i=i+1

x ,y ,r ,n=60,40,30,5

for i in range (0,25):
    r=r-2
    poligonos(x,y,r,n)
    azul

    
pygame.display.flip()
pygame.display.update()    


while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
