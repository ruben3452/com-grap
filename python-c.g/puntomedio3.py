import sys,math,pygame

color=0,0,0
azul=(0,0,255)
tamano= ancho, alto=500,500
pantalla=pygame.display.set_mode(tamano)
pantalla.fill(color)
          
x0, y0, x1, y1 = 90, 0, 90, 200          
xa0, ya0, xa1, ya1 = 0, 0, 90, 90  
xb0, yb0, xb1, yb1 = 180, 150, 90, 90
xc0, yc0, xc1, yc1 = 0, 150, 90, 320


dx = x1 - x0
dy = y1 - y0
p= 2*dy - dx
incE = 2*dy
incNE = 2 * (dy-dx)


if (x0 > x1):
    x = x1
    y = y1
    yend = y0
    xend = x0    
else:
    x = x0
    y = y0
    yend = y1
    xend = x1

if (dy <> 0 and dx == 0):
    while (y <= yend):
        y = y + 1    

        pantalla.set_at((int(x),int(y)), azul)
        pygame.display.flip()
else:
    
    while (x <= xend):

        pantalla.set_at((int(x),int(y)), azul)
        pygame.display.flip()

        if (dy <> 0 and dx <> 0):

            x = x + 1
            if ( p <= 0):
                p = p + incE
                
            else:
                y = y+1
                p = p + incNE


            if ( p >= 0):
                p = p + incE
                
            else:
                y = y-1
                p = p + incNE
          
        elif (dy == 0 and dx <> 0):
            x = x + 1

#____________


dxa = xa1 - xa0
dya = ya1 - ya0
pa= 2*dya - dxa
incEa = 2*dya
incNEa = 2 * (dya-dxa)


if (xa0 > xa1):
    xa = xa1
    ya = ya1
    yenda = ya0
    xenda = xa0    
else:
    xa = xa0
    ya = ya0
    yenda = ya1
    xenda = xa1

if (dya <> 0 and dxa == 0):
    while (ya <= yenda):
        ya = ya + 1    

        pantalla.set_at((int(xa),int(ya)), azul)
        pygame.display.flip()
else:
    
    while (xa <= xenda):

        pantalla.set_at((int(xa),int(ya)), azul)
        pygame.display.flip()

        if (dya <> 0 and dxa <> 0):

            xa = xa + 1
            if ( pa <= 0):
                pa = pa + incEa
                
            else:
                ya = ya+1
                pa = pa + incNEa


            if ( pa >= 0):
                pa = pa + incEa
                
            else:
                ya = ya-1
                pa = pa + incNEa
          
        elif (dya == 0 and dxa <> 0):
            xa = xa + 1
#__________________________________________

dxb = xb1 - xb0
dyb = yb1 - yb0
pb= 2*dyb - dxb
incEb = 2*dyb
incNEb = 2 * (dyb-dxb)


if (xb0 > xb1):
    xb = xb1
    yb = yb1
    yendb = yb0
    xendb = xb0    
else:
    xb = xb0
    yb = yb0
    yendb = yb1
    xendb = xb1

if (dyb <> 0 and dxb == 0):
    while (yb <= yendb):
        yb = yb + 1    

        pantalla.set_at((int(xb),int(yb)), azul)
        pygame.display.flip()
else:
    
    while (xb <= xendb):

        pantalla.set_at((int(xb),int(yb)), azul)
        pygame.display.flip()

        if (dyb <> 0 and dxb <> 0):

            xb = xb + 1
            if ( pb <= 0):
                pb = pb + incEb
                
            else:
                yb = yb+1
                pb = pb + incNEb


            if ( pb >= 0):
                pb = pb + incEb
                
            else:
                yb = yb-1
                pb = pb + incNEb
          
        elif (dyb == 0 and dxb <> 0):
            xb = xb + 1




while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
