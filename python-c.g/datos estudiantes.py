fu= open('directorio.txt','r')
stud1 = fu.readlines()
fu.close()
dict = {}
for i in range(len(stud)):
    linea = stud[i].split(",")
    dict[linea[0]] = linea

print "ingrese la cedula del estudiante "

e=raw_input()
print dict[e]

