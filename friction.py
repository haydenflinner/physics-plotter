from __future__ import division
from visual import *

#Graphics
track =  box(pos=vector(0, -0.05, 0), size=vector(10, 0.05, 0.10), color=color.white)
box = box(pos=vector(13, 2, -2), size=vector(0.1, 0.04, 0.06), color=color.red)

box.m = 23
box.v = vector(4, 0, 0)
dt = 7.5 - 6.0
F = vector(101, 0, 0) # N
frictionfactor = 0.19

def p(box):
    return box.m * box.v

box.p = p(box)

frictionforce = vector(box.m * -9.8 * frictionfactor, 0, 0)
Fnet = (F + frictionforce) * dt
print('Original p', box.p)
print('Original v', box.v)
oldv = box.v
print('Friction force: ', frictionforce)

box.p = box.p + Fnet

print('New p', box.p)
box.v = box.p / box.m
print('new v', box.p / box.m)

print('average v', )
print('new pos', box.pos + ((oldv + box.v)/2)*dt)
