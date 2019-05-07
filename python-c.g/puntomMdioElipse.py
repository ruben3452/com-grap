import sys,math,pygame

color=0,0,0
azul=(0,0,255)
tamano= ancho, alto=500,500
pantalla=pygame.display.set_mode(tamano)
pantalla.fill(color)

def plotpoint (xc,yc,x,y):
    pantalla.set_at((xc+x,  yc +y),azul)
    pantalla.set_at((xc-x,  yc +y),azul)
    pantalla.set_at((xc+x,  yc -y),azul)
    pantalla.set_at((xc-x,  yc -y),azul)


rx, ry, xc, yc = 100, 60, 250, 200 

ry2=ry*ry
rx2=rx*rx

twory2=2*ry2
tworx2=2*rx2
x=0
y=ry
plotpoint(xc,yc,x,y)
pygame.display.flip()
p=round(ry2-rx2*ry+(0.25*rx2))
px=0;
py=tworx2*y
while (px<py):
    x=x+1
    px=px+twory2
    if(p<0):
        p=p+ry2+px
    else:
        y=y-1
        py=py-tworx2
        p=p+ry2+px-py
    plotpoint(xc,yc,x,y)
    pygame.display.flip()
p=round(ry2*(x+0.5)*(x+0.5)+rx2*(y-1)*(y-1)-rx2*ry2)
px=0
py=tworx2*y
while(y>0):
    y=y-1
    py=py-tworx2
    if(p>0):
        p=p+rx2-py
    else:
        x=x+1
        px=px+twory2
        p=p+rx2-py+px
    plotpoint(xc,yc,x,y)
    pygame.display.flip()


while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
