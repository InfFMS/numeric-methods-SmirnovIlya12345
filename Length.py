import math
import numpy as np
import matplotlib.pyplot as plt
# y=0 - линия раздела фаз
print('Enter the coordinates of the starting point and the ending point')
x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
# Частное скоростей света
print('Enter the optic density of the second material relative to the first material')
n=float(input())
where=x1
def optdist(where):
    return np.sqrt((x1-where)**2+y1**2)+n*np.sqrt((x2-where)**2+y2**2)
while optdist(where)>optdist(where+(x2-x1)/1000):
    where+=(x2-x1)/1000
    print(where,optdist(where))
print(where)
print('Angle:', np.atan(y1/where))
xfirst=np.linspace(x1,where,2)
xsecond=np.linspace(where,x2,2)
xgeneral=np.linspace(x1,x2,1000)
yfirst=-xfirst*y1/(where-x1)+where*y1/(where-x1)
ysecond=xsecond*y2/(x2-where)-x2*y2/(x2-where)
y0=0*xgeneral
plt.plot(xfirst, yfirst, color="blue")
plt.plot(xsecond, ysecond+y2, color="red")
plt.plot(xgeneral, y0, color="black")
plt.show()
ythird=optdist(xgeneral)
plt.plot(xgeneral, ythird, color="black")
plt.show()
print('Synes of falling and broken angles are:',(where-x1)/np.sqrt((where-x1)**2+y1**2),(x2-where)*np.sqrt((x2-where)**2+y2**2))
if (where-x1)/np.sqrt((where-x1)**2+y1**2)>n*(x2-where)/np.sqrt((x2-where)**2+y2**2)*0.99 and (where-x1)/np.sqrt((where-x1)**2+y1**2)<n*(x2-where)/np.sqrt((x2-where)**2+y2**2)*1.01:
    print("Snell's law works!")
