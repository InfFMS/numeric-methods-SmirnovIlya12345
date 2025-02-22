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
for i in range(len(b)):
    A=b[i]**2
    B=c[i]*b[i]*2
d=B/2/A
print('Resistance is: ',d)
fig,ax=plt.subplots()
plt.scatter(b,c)
x=[0,3]
y=[0,3*d]
plt.plot(x, y, color="blue")
plt.show()
