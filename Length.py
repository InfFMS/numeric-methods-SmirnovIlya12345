import math
import numpy as np
import matplotlib.pyplot as plt
print('Enter the coordinates of the starting point and the ending point')
x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
print('Enter the optic density of the second material relative to the first material')
n=float(input())
where1=x1
where2=x2
while True:
    if where2-where1>0.000001:
        optdist1=math.sqrt((x1-where1)**2+y1**2)+math.sqrt((x2-where1)**2+(-y2)**2)*n
        optdist2=math.sqrt((x1-where2)**2+y1**2)+math.sqrt((x2-where2)**2+(-y2)**2)*n
        if optdist1<optdist2:
            where2=where2*0.8+where1*0.2
        else:
            where1=where1*0.8+where2*0.2
    else:
        where=where1*0.5+where2*0.5
        break
print(where)
x=np.linspace(x1,where,2)
x2=np.linspace(where,x2,2)
y1=-x*(y1/(where-x1))+y1/(where-x1)*where
y2=x*(y2/(x2-where))-y2/(x2-where)
plt.plot(x, y1, color="blue")
plt.plot(x, y2, color="red")
plt.show()
