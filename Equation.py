import math
leng1=0.0
leng2=0.0
leng3=0.0
leng4=0.0
for i in range(31416):
    leng1+=math.sqrt(1/100000000+(math.cos(i/10000)-math.cos((i-1)/10000))**2)
    leng2+=math.sqrt(1/100000000+(math.cos(i/10000)-math.cos((i-1)/10000)+(0.1*((i/10000)**2))-(0.1*((i-1)/10000)**2))**2)
    leng3+=math.sqrt(1/100000000+(math.tanh(i/10000-1.5708)-math.tanh((i-1)/10000-1.5708))**2)
    leng4+=math.sqrt(1/100000000+(-0.2*((i/10000-3.1416)**3)+0.5*((i/10000-3.1416)**2)+0.2*(((i-1)/10000-3.1416)**3)-0.5*(((i-1)/10000-3.1416)**2))**2)
print(leng1,leng2,leng3,leng4)
