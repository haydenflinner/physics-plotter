from __future__ import division
from visual import *
import matplotlib.pyplot as plt

#Graphics
track =  box(pos=vector(0, -0.05, 0), size=vector(10, 0.05, 0.10), color=color.white)
carts = [box(pos=vector(-5 + 0.05, 0, 0), size=vector(0.1, 0.04, 0.06), color=color.red),
box(pos=vector(-5 + 0.05, 0.5, 0), size=vector(0.1, 0.15, 0.06), color=color.red)]

#Initial cond.
carts[0].F = vector(1.123, 0, 0)
carts[1].F = vector(1, 0, 0)
carts[0].duration = 1
carts[1].duration = 4.46
for cart in carts:
    cart.m = 1
    cart.v = vector(0, 0, 0)
    cart.p = cart.v
    cart.p_a = []
    cart.r_a = []
    cart.a_a = []
    
deltat = 0.01
t = 0
marker = None
ta = []
print(carts[0].pos.x)
while t < carts[1].duration:
    rate(100)
    for cart in carts:
        Fnet = cart.F * deltat
        if cart == carts[0] and cart.pos.x > 0:
            Fnet = vector(0,0,0)
        cart.p = cart.p + Fnet
        cart.pos = cart.pos + (cart.p/cart.m) * deltat
        cart.p_a.append(cart.p.x)
        cart.r_a.append(cart.pos.x)
        cart.a_a.append(Fnet)
    # Used to see how far off my old model was
    if abs(t - 4.46/2) < 0.001 and not marker:
        marker = box(pos=carts[0].pos, size=carts[0].size, color=color.blue)
    # When they meet, break
    if abs(carts[0].pos.x - carts[1].pos.x) < 0.001 and t > 3:
        for cart in carts:
            cart.color = color.white
        break
    ta.append(t)
    t = t + deltat

plt.figure(1)
plt.ylim(0)
plt.subplot(211)
plt.plot(ta, carts[0].p_a, 'ro')
plt.plot(ta, carts[1].p_a, 'bo')

plt.subplot(211)
plt.plot(ta, carts[0].r_a, 'ro')
plt.plot(ta, carts[1].r_a, 'bo')

plt.subplot(212)
plt.ylim(0, 0.1)
plt.plot(ta, carts[0].a_a, 'ro')
plt.plot(ta, carts[1].a_a, 'bo')
plt.show()
