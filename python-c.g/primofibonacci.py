import math
cont=0
cont2=0
fib=[]
a, b = 0, 1
while b < 10000:    
    fib.append(b)  
    a, b = b, a+b

print(fib)
        
for n in fib:
    if n <=1:
        cont +=0
        #return False
    elif n ==2:
        cont +=1
        #return True
    elif n % 2 ==0:
        cont +=0
        #return False
    else:
        for i in range(3, int(math.sqrt(n)),2):
            if n % i ==0:
                cont +=0
                #return False
            break
        else:
            cont +=1
            #return True

print ('los numeros primos que hay en febonacci son:', cont)
