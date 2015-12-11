# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 09:34:24 2015

@author: albert
"""

from __future__ import division, print_function
from pylab import*
from scipy.integrate import simps
import time

start_time = time.time()

interactive(True)
close('All')

long_ona,x,y,z,espectre=loadtxt('arxiu_problema.txt', delimiter=' ', usecols=(0,1,2,3,4), unpack=True)

  

def rgb(long_ona,x,y,z,espectre):
    xE=x*espectre
    yE=y*espectre
    zE=z*espectre
    
    x1=simps(xE,long_ona)
    y1=simps(yE,long_ona)
    z1=simps(zE,long_ona)
    
    xyz=[x1,y1,z1]
    
    xx=x1/(x1+y1+z1)
    yy=y1/(x1+y1+z1)
    zz=z1/(x1+y1+z1)
    
    xxyyzz=[xx,yy,zz]
    
    canvi=[[3.240479,-1.537150,-0.498535],
           [-0.969256,1.875992,0.041556],
           [0.055648,-0.204043,1.057311]]
    
    CIE=[xx,yy,zz]
    
    r=uint8(255*dot(canvi[0],CIE))
    g=uint8(255*dot(canvi[1],CIE))
    b=uint8(255*dot(canvi[2],CIE))
        
    N=256
    cl=ones([N,N,3])
    cl[:,:,0]*=r
    cl[:,:,1]*=g
    cl[:,:,2]*=b
    
    rgb=[r,g,b]
    
    print('x,y,z ='+str(xyz))
    print('X,Y,Z ='+str(xxyyzz))
    print('R,G,B ='+str(rgb))
    
    return cl


cl_espectre=rgb(long_ona,x,y,z,espectre)

print('Si es prenem E=1:\n')

espectre_ones=ones(espectre.shape)

cl_ones=rgb(long_ona,x,y,z,espectre_ones)

figure()
subplot(211)
plot(long_ona, x, label='x')
plot(long_ona, y, label='y')
plot(long_ona, z, label='z')
xlim(380,650)
ylim(0,2)
legend()

subplot(212)
plot(long_ona, espectre)
xlim(380,650)
ylim(0,2)


figure()
imshow(cl_espectre)

figure()
imshow(cl_ones)

time=time.time()-start_time
print("runing time ="+str(time))