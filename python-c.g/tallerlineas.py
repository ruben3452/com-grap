
import pygame, sys

pygame.init()

visor=pygame.display.set_mode((400,400),0,32)

negro=(0,0,0)
rojo=(255,0,0)
azul=(0,0,255)
morado=(128,0,128)
lista=[negro,rojo,azul,morado]

visor.fill(lista[0])
#punto 1.1 casa
pygame.draw.line(visor,lista[3],(50, 50),(70, 70),4)
pygame.draw.line(visor,lista[3],(50,50),(30,70),4)
pygame.draw.line(visor,lista[2],(30,70),(70,70),4)
pygame.draw.line(visor,lista[2],(30,100),(30,70),4)
pygame.draw.line(visor,lista[2],(30,100),(70,100),4)
pygame.draw.line(visor,lista[2],(70,100),(70,70),4)
pygame.draw.line(visor,lista[2],(40,100),(40,80),4)
pygame.draw.line(visor,lista[2],(40,80),(50,80),4)
pygame.draw.line(visor,lista[2],(50,100),(50,80),4)
#-----------muñeca---------------------------------
pygame.draw.line(visor,lista[1],(90,100),(90,90),4)
pygame.draw.line(visor,lista[1],(90,100),(100,100),4)
pygame.draw.line(visor,lista[1],(100,100),(100,90),4)
pygame.draw.line(visor,lista[1],(100,90),(90,90),4)
pygame.draw.line(visor,lista[1],(95,110),(95,100),4)
pygame.draw.line(visor,lista[1],(95,110),(110,100),4)
pygame.draw.line(visor,lista[1],(95,110),(80,100),4)
pygame.draw.line(visor,lista[1],(95,110),(105,120),4)
pygame.draw.line(visor,lista[1],(95,110),(85,120),4)
pygame.draw.line(visor,lista[1],(85,120),(105,120),4)
pygame.draw.line(visor,lista[1],(90,130),(90,120),4)
pygame.draw.line(visor,lista[1],(100,130),(100,120),4)
#punto 1.2 muñeco
pygame.draw.line(visor,lista[2],(150,100),(150,90),4)
pygame.draw.line(visor,lista[2],(150,100),(160,100),4)
pygame.draw.line(visor,lista[2],(160,100),(160,90),4)
pygame.draw.line(visor,lista[2],(160,90),(150,90),4)
pygame.draw.line(visor,lista[2],(155,110),(155,100),4)
pygame.draw.line(visor,lista[2],(155,110),(170,100),4)
pygame.draw.line(visor,lista[2],(155,110),(140,100),4)
pygame.draw.line(visor,lista[2],(180,110),(170,100),4)
pygame.draw.line(visor,lista[2],(180,110),(190,80),4)

pygame.draw.line(visor,lista[2],(190,80),(180,70),4)
pygame.draw.line(visor,lista[2],(190,80),(200,70),4)
pygame.draw.line(visor,lista[2],(200,70),(190,60),4)
pygame.draw.line(visor,lista[2],(180,70),(190,60),4)
pygame.draw.line(visor,lista[2],(180,70),(200,70),4)
pygame.draw.line(visor,lista[2],(190,60),(190,80),4)

pygame.draw.line(visor,lista[2],(150,120),(150,110),4)
pygame.draw.line(visor,lista[2],(150,120),(160,120),4)
pygame.draw.line(visor,lista[2],(160,120),(160,110),4)
pygame.draw.line(visor,lista[2],(160,110),(150,110),4)
pygame.draw.line(visor,lista[2],(149,130),(152,120),4)
pygame.draw.line(visor,lista[2],(162,130),(154,120),4)
#punto 1.3
pygame.draw.line(visor,lista[3],(240,120),(240,90),4)
pygame.draw.line(visor,lista[3],(240,120),(270,120),4)
pygame.draw.line(visor,lista[3],(270,120),(270,90),4)
pygame.draw.line(visor,lista[3],(270,90),(240,90),4)
pygame.draw.line(visor,lista[3],(255,90),(255,60),4)
pygame.draw.line(visor,lista[3],(255,60),(350,60),4)
pygame.draw.line(visor,lista[3],(350,90),(350,60),4)
pygame.draw.line(visor,lista[3],(350,90),(320,90),4)
#punto 1.4
pygame.draw.line(visor,lista[3],(190,210),(100,210),4)
pygame.draw.line(visor,lista[3],(190,210),(190,270),4)
pygame.draw.line(visor,lista[3],(190,270),(100,270),4)
pygame.draw.line(visor,lista[3],(100,270),(100,210),4)

pygame.draw.line(visor,lista[2],(160,250),(160,270),4)
pygame.draw.line(visor,lista[2],(130,250),(130,270),4)
pygame.draw.line(visor,lista[2],(130,250),(160,250),4)

pygame.draw.line(visor,lista[3],(145,190),(160,210),4)
pygame.draw.line(visor,lista[3],(145,190),(130,210),4)
pygame.draw.line(visor,lista[3],(145,190),(145,160),4)
pygame.draw.line(visor,lista[3],(130,170),(160,170),4)

pygame.draw.line(visor,lista[2],(170,230),(170,250),4)
pygame.draw.line(visor,lista[2],(170,230),(190,230),4)
pygame.draw.line(visor,lista[2],(170,250),(190,250),4)

pygame.draw.line(visor,lista[2],(120,230),(120,250),4)
pygame.draw.line(visor,lista[2],(100,230),(120,230),4)
pygame.draw.line(visor,lista[2],(100,250),(120,250),4)
pygame.display.update()


while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
       pygame.quit()
