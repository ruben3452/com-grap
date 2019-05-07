import sys,math,pygame

color = 255, 255 , 255 


azul = (0,0,255)
tamano = ancho, alto = 500, 500
pantalla = pygame.display.set_mode(tamano)
pantalla.fill(color)

def plotpoint(xc,yc,x,y):
    pantalla.set_at((xc + x,yc + y),azul)
    pantalla.set_at((xc - x,yc + y),azul)
    pantalla.set_at((xc + x,yc - y),azul)
    pantalla.set_at((xc - x,yc - y),azul)
    pantalla.set_at((xc + y,yc + x),azul)
    pantalla.set_at((xc - y,yc + x),azul)
    pantalla.set_at((xc + y,yc - x),azul)
    pantalla.set_at((xc - y,yc - x),azul)

xc=input('ingrese numero para xc')
yc=input('ingrese numero para yc')
r=input('ingrese numero para r')


x=0
y=r
p=1 - r
plotpoint(xc,yc,x,y)
while(x<y):
    x=x+1
    if(p<0):
        p=p+2*x+1
    else:
        y=y-1
        p=p+2*(x-y)+1
    plotpoint(xc,yc,x,y)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  
