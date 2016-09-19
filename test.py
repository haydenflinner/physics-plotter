from __future__ import division
from visual import *
import matplotlib.pyplot as plt

#Graphics
track =  box(pos=vector(0, -0.05, 0), size=vector(10, 0.05, 0.10), color=color.white)
carts = [box(pos=vector(0, 0, 0), size=vector(0.1, 0.1, 0.1), color=color.red),
box(pos=vector(-5 + 0.05, 0, 0), size=vector(0.1, 0.04, 0.06), color=color.red),
box(pos=vector(-5 + 0.05, 0.5, 0), size=vector(0.1, 0.15, 0.06), color=color.red)]

#Initial cond.
carts[1].F = vector(1.123, 0, 0)
carts[2].F = vector(1, 0, 0)
carts[1].duration = 1
carts[2].duration = 4.46
for cart in carts:
    cart.m = 1
    cart.v = vector(0, 0, 0)
    cart.p = cart.v
    

p1 = []
r1 = []
a1 = []
p2 = []
r2 = []
a2 = []
ta = []
deltat = 0.01
t = 0
marker = None

print(carts[1].pos.x)
while t < carts[2].duration:
    rate(10000)
    if carts[1].pos.x < 0:
        carts[1].p = carts[1].p  + carts[1].F * deltat
        a1.append(carts[1].F.x * deltat)
    else:
        a1.append(0)
    carts[2].p = carts[2].p  + carts[2].F * deltat
    carts[2].pos = carts[2].pos + (carts[2].p/carts[2].m) * deltat
    carts[1].pos = carts[1].pos + (carts[1].p/carts[1].m) * deltat
    # When they meet, break
    if abs(t - 4.46/2) < 0.001 and not marker:
        marker = box(pos=carts[1].pos, size=carts[0].size, color=color.blue)
    if abs(carts[1].pos.x - carts[2].pos.x) < 0.001 and t > 3:
        for cart in carts:
            cart.color = color.white
        break

    p1.append(carts[1].p.x)
    r1.append(carts[1].pos.x)
    p2.append(carts[2].p.x)
    r2.append(carts[2].pos.x)
    a2.append(carts[2].F.x * deltat)
    ta.append(t)
    t = t + deltat
plt.figure(1)
plt.ylim(0)
plt.subplot(211)
plt.plot(ta, p1, 'ro')
plt.plot(ta, p2, 'bo')

plt.subplot(211)
plt.plot(ta, r1, 'ro')
plt.plot(ta, r2, 'bo')

plt.subplot(212)
plt.ylim(0, 0.1)
plt.plot(ta, a1, 'ro')
plt.plot(ta, a2, 'bo')
plt.show()
