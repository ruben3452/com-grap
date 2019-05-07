import sys,math,pygame

color=0,0,0
azul=(0,0,255)
tamano= ancho, alto=500,500
pantalla=pygame.display.set_mode(tamano)
pantalla.fill(color)
          
x0, y0, x1, y1 = 90, 30, 90, 190          
xa0, ya0, xa1, ya1 = 0, 280, 90, 90  
xb0, yb0, xb1, yb1 = 180, 170, 90, 190
xc0, yc0, xc1, yc1 = 0, 120, 180, 120
xct, yct ,rt= 90,80 ,20
xd0, yd0, xd1, yd1 = 90, 30, 280, 30
xe0, ye0, xe1, ye1 = 280, 30, 280, 340
xf0, yf0, xf1, yf1 = 0, 340, 500, 340


#________________________cuerpo____________________________________
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

#____________pierna1


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
#_______________________pierna2___________________

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


#__________________brazos________________________

dxc = xc1 - xc0
dyc = yc1 - yc0
pc= 2*dyc - dxc
incEc = 2*dyc
incNEc = 2 * (dyc-dxc)


if (xc0 > xc1):
    xc = xc1
    yc = yc1
    yendc = yc0
    xendc = xc0    
else:
    xc = xc0
    yc = yc0
    yendc = yc1
    xendc = xc1

if (dyc <> 0 and dxc == 0):
    while (yc <= yendc):
        yc = yc + 1    

        pantalla.set_at((int(xc),int(yc)), azul)
        pygame.display.flip()
else:
    
    while (xc <= xendc):

        pantalla.set_at((int(xc),int(yc)), azul)
        pygame.display.flip()

        if (dyc <> 0 and dxc <> 0):

            xc = xc + 1
            if ( pc <= 0):
                pc = pc + incEc
                
            else:
                yc = yc+1
                pc = pc + incNEc


            if ( pc >= 0):
                pc = pc + incEc
                
            else:
                yc = yc-1
                pc = pc + incNEc
          
        elif (dyc == 0 and dxc <> 0):
            xc = xc + 1

#-------------------cabeza----------------------------------------------


def plotpoint(xc,yc,x,y):
    pantalla.set_at((xc + x,yc + y),azul)
    pantalla.set_at((xc - x,yc + y),azul)
    pantalla.set_at((xc + x,yc - y),azul)
    pantalla.set_at((xc - x,yc - y),azul)
    pantalla.set_at((xc + y,yc + x),azul)
    pantalla.set_at((xc - y,yc + x),azul)
    pantalla.set_at((xc + y,yc - x),azul)
    pantalla.set_at((xc - y,yc - x),azul)




xt=0
yt=rt
pt=1 - rt
plotpoint(xct,yct,xt,yt)
while(xt<yt):
    xt=xt+1
    if(pt<0):
        pt=pt+2*xt+1
    else:
        yt=yt-1
        pt=pt+2*(xt-yt)+1
    plotpoint(xct,yct,xt,yt)

pygame.display.flip()

#_______________soporte1___________________________

dxd = xd1 - xd0
dyd = yd1 - yd0
pd= 2*dyd - dxd
incEd = 2*dyd
incNEd = 2 * (dyd-dxd)


if (xd0 > xd1):
    xd = xd1
    yd = yd1
    yendd = yd0
    xendd = xd0    
else:
    xd = xd0
    yd = yd0
    yendd = yd1
    xendd = xd1

if (dyd <> 0 and dxd == 0):
    while (yd <= yendd):
        yd = yd + 1    

        pantalla.set_at((int(xd),int(yd)), azul)
        pygame.display.flip()
else:
    
    while (xd <= xendd):

        pantalla.set_at((int(xd),int(yd)), azul)
        pygame.display.flip()

        if (dyd <> 0 and dxd <> 0):

            xd = xd + 1
            if ( pd <= 0):
                pd = pd + incEd
                
            else:
                yd = yd+1
                pd = pd + incNEd


            if ( pd >= 0):
                pd = pd + incEd
                
            else:
                yd = yd-1
                pd = pd + incNEd
          
        elif (dyd == 0 and dxd <> 0):
            xd = xd + 1

#_______________poste___________________________

dxe = xe1 - xe0
dye = ye1 - ye0
pe= 2*dye - dxe
incEe = 2*dye
incNEe = 2 * (dye-dxe)


if (xe0 > xe1):
    xe = xe1
    ye = ye1
    yende = ye0
    xende = xe0    
else:
    xe = xe0
    ye = ye0
    yende = ye1
    xende = xe1

if (dye <> 0 and dxe == 0):
    while (ye <= yende):
        ye = ye + 1    

        pantalla.set_at((int(xe),int(ye)), azul)
        pygame.display.flip()
else:
    
    while (xe <= xende):

        pantalla.set_at((int(xe),int(ye)), azul)
        pygame.display.flip()

        if (dye <> 0 and dxe <> 0):

            xe = xe + 1
            if ( pe <= 0):
                pe = pe + incEe
                
            else:
                ye = ye+1
                pe = pe + incNEe


            if ( pe >= 0):
                pe = pe + incEe
                
            else:
                ye = ye-1
                pe = pe + incNEe
          
        elif (dye == 0 and dxe <> 0):
            xe = xe + 1

#_______________piso___________________________

dxf = xf1 - xf0
dyf = yf1 - yf0
pf= 2*dyf - dxf
incEf = 2*dyf
incNEf = 2 * (dyf-dxf)


if (xf0 > xf1):
    xf = xf1
    yf = yf1
    yendf = yf0
    xendf = xf0    
else:
    xf = xf0
    yf = yf0
    yendf = yf1
    xendf = xf1

if (dyf <> 0 and dxf == 0):
    while (yf <= yendf):
        yf = yf + 1    

        pantalla.set_at((int(xf),int(yf)), azul)
        pygame.display.flip()
else:
    
    while (xf <= xendf):

        pantalla.set_at((int(xf),int(yf)), azul)
        pygame.display.flip()

        if (dyf <> 0 and dxf <> 0):

            xf = xf + 1
            if ( pf <= 0):
                pf = pf + incEf
                
            else:
                yf = yf+1
                pf = pf + incNEf


            if ( pf >= 0):
                pf = pf + incEf
                
            else:
                yf = yf-1
                pf = pf + incNEf
          
        elif (dyf == 0 and dxf <> 0):
            xf = xf + 1

while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
