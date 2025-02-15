import numpy as np
import matplotlib.pyplot as plt
f=open('data.csv', 'r', encoding='utf-8')
lines=[line for line in f]
b=[0]*10
c=[0]*10
for j in range(1,len(lines)):
    b[j-1]=float(lines[j].split(',')[0])
    c[j-1]=float(lines[j].split(',')[1])
print(b,c)
d=3.14
while True:
    def error(weight):
        err=0.0
        for i in range(10):
            err+=(b[i]*weight-c[i])**2
        return err
    if error(d+0.01)<error(d):
        d=d+0.01
    elif error(d-0.01)<error(d):
        d=d-0.01
    else:
        print('Resistance is', round(d,2))
        break
fig,ax=plt.subplots()
plt.scatter(b,c)
x=[0,3]
y=[0,3*d]
plt.plot(x, y, color="blue")
plt.show()
