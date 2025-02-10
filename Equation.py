import math
import numpy as np
import matplotlib.pyplot as plt
leng1=0.0
leng2=0.0
leng3=0.0
leng4=0.0
for i in range(31416):
    leng1+=math.sqrt(1/100000000+(math.cos(i/10000)-math.cos((i-1)/10000))**2)
    leng2+=math.sqrt(1/100000000+(math.cos(i/10000)-math.cos((i-1)/10000)+(0.1*((i/10000)**2))-(0.1*((i-1)/10000)**2))**2)
    leng3+=math.sqrt(1/100000000+(math.tanh(i/10000-1.5708)-math.tanh((i-1)/10000-1.5708))**2)
    leng4+=math.sqrt(1/100000000+(-0.2*((i/10000-3.1416)**3)+0.5*((i/10000-3.1416)**2)+0.2*(((i-1)/10000-3.1416)**3)-0.5*(((i-1)/10000-3.1416)**2))**2)
print("Curves' length are:",leng1,leng2,leng3,leng4)
fig, axs = plt.subplots(1, 4, figsize=(10, 4))
x=np.linspace(0,3.1415926535897932384626433832795028841971693993751,100)
y0=np.cos(x)
y1=np.cos(x)-0.1*x**2
y2=-np.tanh(x-3.14159265/2)
y3=-0.2*(x-3.14159265/2)**3+0.5*(x-3.14159265/2)**2+1
axs[0].plot(x, y0, color="red")
axs[0].set_title("y = cos(x)")
axs[1].plot(x, y1, color="red")
axs[1].set_title("y = cos(x)-x**2")
axs[2].plot(x, y2, color="red")
axs[2].set_title("y = tanh(x-pi/2)")
axs[3].plot(x, y3, color="red")
axs[3].set_title("y = -0.2*(x-pi/2)**3+0.5*(x-pi/2)**2+1")
plt.show()
