import sys,math,pygame

color=0,0,0
azul=(0,0,255)
tamano= ancho, alto=500,500
pantalla=pygame.display.set_mode(tamano)
pantalla.fill(color)

x ,y ,r ,n=60,40,30,5


a=math.pi/2-math.pi/n
x1=int(x-r*math.cos(a))
y1=int(y+r*math.sin(a))
pantalla.set_at((x,y), azul)
pygame.display.flip()
i=0
while(i<n+1):
    a=a+2*math.pi/n
    x2=int(x-r*math.cos(a))
    y2=int(y+r*math.sin(a))
    pantalla.set_at((x1,y1), azul)
    pygame.draw.line(pantalla,azul,(x1, y1),(x2, y2),6)
    pygame.display.flip()
    x1=x2
    y1=y2
    i=i+1


while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
