import math
import numpy as np
import matplotlib.pyplot as plt
area1=0
area2=0
area3=0
area4=0
area5=0
a_lot=10000
for i in range(int(round(np.pi*a_lot,0))):
    area1+=abs(math.sin(2*(i/a_lot))+0.5-0.2*i*i/(a_lot**2))/a_lot
for i in range(int(round(np.pi*a_lot/2,0)),int(round(np.pi*a_lot/2,0))):
    area2+=abs(math.cos(i/a_lot)+0.5-0.5*i*i/(a_lot**2))/a_lot
for i in range(-20000,20000):
    area3+=abs(math.e**(-i*i/(a_lot**2))+0.5-0.3*((i/a_lot)**3))/a_lot
    area4+=abs(math.e**(-i*i/(a_lot**2))+1-0.2*math.sin(3*i/a_lot))/a_lot
    area5+=abs(math.e**(-(i+a_lot)*(i+a_lot)/(a_lot**2))+math.e**(-(i-a_lot)*(i-a_lot)/(a_lot**2))+0.5-0.3*i*i/(a_lot**2))/a_lot
print("Klyaksys' areas are:",area1,area2,area3,area4,area5)
fig, axs = plt.subplots(1, 5, figsize=(10, 4))
x=np.linspace(0,3.1416,100)
x2=np.linspace(-1.5708,1.5708,100)
x3=np.linspace(-2,2,100)
y00=np.sin(2*x)+1
y01=-0.2*x**2+0.5
y10=np.cos(x2)+1.2
y11=-0.5*x2**2+0.7
y20=np.exp((-x3**2))+1
y21=-0.3*x3**3-0.5
y30=np.exp((-x3**2))+0.5
y31=0.2*np.sin(3*x3)-0.5
y40=np.exp((-((x3+1)**2)))+np.exp((-((x3-1)**2)))+0.5
y41=-0.3*x3**2
axs[0].plot(x, y00, color="blue")
axs[0].plot(x, y01, color="blue")
axs[0].set_title("y = -0.2*x**2+0.5, y = sin(2*x)+1")
axs[1].plot(x2, y10, color="blue")
axs[1].plot(x2, y11, color="blue")
axs[1].set_title("y = -0.5*x**2+0.7, y = cos(x)+1.2")
axs[2].plot(x3, y20, color="blue")
axs[2].plot(x3, y21, color="blue")
axs[2].set_title("y = -0.3*x**3+0.5, y = e**(-x**2)+1")
axs[3].plot(x3, y30, color="blue")
axs[3].plot(x3, y31, color="blue")
axs[3].set_title("y = -0.3*x**3+0.5, y = 0.2*sin(3*x)-0.5")
axs[4].plot(x3, y40, color="blue")
axs[4].plot(x3, y41, color="blue")
axs[4].set_title("y = e**(-(x+1)**2)+e**(-(x-1)**2)+0.5, y = 0.3*x**2")
plt.show()
plt.show()
plt.show()
plt.show()
plt.show()
