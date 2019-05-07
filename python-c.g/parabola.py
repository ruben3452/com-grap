import sys,math,pygame

color=0,0,0
azul=(0,0,255)
tamano= ancho, alto=400,400
pantalla=pygame.display.set_mode(tamano)
pantalla.fill(color)


def plotpoint (x,y):
    pantalla.set_at((x,y),azul)
    pantalla.set_at((x,-y),azul)
   

k=3
x=10
y=100
p=3


plotpoint(x,y)
pygame.display.flip()
while(x <=300):
    x=x+1
    if(p>0):
        y=y+1
        #p=p-2*y+1
        p=int(p+(1+2*(k-1/2))*2)
    else:
        p=int (p-(2 *y *k)+2*(k-1/2)+2*(k-1/2)*2)
    plotpoint(x,y)
    pygame.display.flip()
#pk=pk+1+2(k-1/2)*2 caso p<0
#pk=pk-2yk+2(k-1/2)+2(k- 1/2)*2

while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()



