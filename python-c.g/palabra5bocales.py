fu= open('textox.txt','r')
fras = fu.readline()
fu.close()
listad = fras.split()
for indice, pal in enumerate(listad):
    print "La palabra numero", indice, "(", pal, ") numero de bocales" ,
    print pal.count('a')+pal.count('e')+pal.count('i')+pal.count('o')+pal.count('u')
