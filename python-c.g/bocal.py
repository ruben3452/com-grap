palabra=[]
let=0
print 'ingrese la palabra que desea analizar: '
palabra = raw_input()
print (palabra)
for bocal in palabra:
    if bocal=='a':
        let += 1
        print("a-1")
    if bocal=='e':
        let += 1
        print("e-1")
    if bocal=='i':
        let += 1
        print("i-1")
    if bocal=='o':
        let += 1
        print("o-1")
    if bocal=='u':
        let += 1
        print("u-1")
print ("Cantidad de vocales en la palabra:", let)
