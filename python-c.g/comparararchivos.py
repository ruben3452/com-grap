fu = open("archivopalabraA.txt","r")
for archivoA in fu.readlines():
     archivoA = archivoA.split()
print archivoA


fu2 = open("archivopalabraB.txt","r")
for archivoB in fu2.readlines():
    archivoB = archivoB.split()
print archivoB



cont = 0

for p in archivoA:
    for q in archivoB:
            if p == q:
                 cont = cont+1
print "los dos Archivos tienen",cont," palabras iguales"

fu.close()
fu2.close()

    
