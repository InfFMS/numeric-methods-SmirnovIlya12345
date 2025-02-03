from math import log
from math import cos
import numpy
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
