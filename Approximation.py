from math import log
from math import cos
import numpy as np
import matplotlib.pyplot as plt
def expression0(a):
    return a**3-a+1
def expression1(a):
    return a**3-a**2-a*9+9
def expression2(a):
    return a**2-2.718281828**a
def expression3(a):
    return 5*a-6*log(a,2.718281828)-7
def expression4(a):
    return cos(a)+2*a-3
maxmins0=[]
maxmins1=[]
maxmins2=[]
maxmins3=[]
maxmins4=[]
new=-10
for i in range(-1000,1000):
    if expression0(new)*expression0(i/100)<0:
        maxmins0.append(i/100)
        new=i/100
print(maxmins0)
new=-10
for i in range(-1000,1000):
    if expression1(new)*expression1(i/100)<0:
        maxmins1.append(i/100)
        new=i/100
print(maxmins1)
new=-10
for i in range(-1000,1000):
    if expression2(new)*expression2(i/100)<0:
        maxmins2.append(i/100)
        new=i/100
print(maxmins2)
new=0.1
for i in range(1,1000):
    if expression3(new)*expression3(i/100)<0:
        maxmins3.append(i/100)
        new=i/100
print(maxmins3)
new=-10
for i in range(-1000,1000):
    if expression4(new)*expression4(i/100)<0:
        maxmins4.append(i/100)
        new=i/100
print(maxmins4)
fig, axs = plt.subplots(1, 4, figsize=(10, 4))
x=np.linspace(-10,10,100)
x2=np.linspace(0.01,10,100)
x3=np.linspace(-10,5,100)
y0=x**3-x+1
y1=x**3-x*2-9*x+9
y2=x3**2-2.718281828**x3
y4=np.cos(x)+2*x-3
axs[0].plot(x, y0, color="blue")
axs[0].set_title("y = x**3-x+1")
axs[1].plot(x, y1, color="blue")
axs[1].set_title("y = a**3-a**2-a*9+9")
axs[2].plot(x3, y2, color="blue")
axs[2].set_title("y = x**2-2.718281828**x")
axs[3].plot(x, y4, color="blue")
axs[3].set_title("y = cos(x)+2*x-3")
plt.show()
