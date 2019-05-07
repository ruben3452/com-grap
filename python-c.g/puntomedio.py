import sys,math,pygame

color=0,0,0
azul=(0,0,255)
tamano= ancho, alto=500,500
pantalla=pygame.display.set_mode(tamano)
pantalla.fill(color)

x1=input('ingrese numero para x1')
y1=input('ingrese numero para y1')
x2=input('ingrese numero para x2')
y2=input('ingrese numero para y2')

dx=x2 - x1
dy=y2-y1
p=2*dy
incE=2*dy
incNE =2*(dy-dx)

if(x1>x2):
    x=x2
    y=y2
    xend=x1
else:
    x=x1
    y=y1
    xend=x2

while(x<=xend):
    pantalla.set_at((int(x),int(y)),azul)
    pygame.display.flip()
    x=x+1
    if(p<=0):
        p=p+incE
    else:
        y=y+1
        p=p+incNE

while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
