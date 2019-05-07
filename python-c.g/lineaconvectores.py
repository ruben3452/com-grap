import sys,math,pygame
xa = input("ingrese xa")
ya = input("ya")
xb = input("xb")
yb = input("yb")
colorfondo = 255, 255, 255
tamano = ancho, alto = 500, 500
pantalla = pygame.display.set_mode(tamano)
pantalla.fill(colorfondo)



#xa, ya = 100, 15
#xb, yb = 39, 399
uncolor = 255, 0, 0
dx= xb - xa
dy= yb - ya
numeropasos = abs(dy)
if abs(dx) > abs(dy):
    numeropasos = abs(dx)
    incrementox = incrementoy = 0
if numeropasos <> 0:
# no dividirás por cero
    incrementox = 1.0*dx/numeropasos
# 1.0 garantiza división flotante
    incrementoy = 1.0*dy/numeropasos
    x,y = xa, ya
# punto inicial
    pantalla.set_at((int(x), int(y)), uncolor)
for k in range(numeropasos):
    x = x + incrementox
    y = y + incrementoy
    pantalla.set_at((int(x),int(y)), uncolor)
    pygame.display.flip()
    corre = 1
while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
       pygame.quit()

    

