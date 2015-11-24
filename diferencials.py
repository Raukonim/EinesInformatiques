# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 09:43:19 2015

@author: albert
"""

from __future__ import division
from pylab import*
from scipy.integrate import odeint
import time

start_time = time.time()

interactive(True)
close('All')

def eqdif(y,t):
    """
    y[0]=velocitat
    y[1]=angle
    y[2]=temps
    """
    g=9.8
    L=10
    m=1
    b=0.3
    omega=0.2
    amp=0.5
    
    return  (-g*sin(y[1])/L)+(-b*y[0]+amp*cos(omega*t)/(m*L*L)), y[0]

t=arange(0,10,0.1)
y0_0 = 0
y1_0 = 1
y0=[y0_0, y1_0]

y=odeint(eqdif, y0, t)

figure()
subplot(2,1,1)
title('Harmonic driven forced oscillator')
xlabel('temps')
ylabel('Omega')
plot(t,y[:,0])

subplot(2,1,2)
xlabel('temps')
ylabel('Theta')
plot(t,y[:,1])

def central(x,t):
    """
    x[0]=velocitat x
    x[1]=posicio x
    
    x[2]=velocitat y
    x[3]=posició y
    """
    G=6.67408*10**(-11)
    M=5.97219*10**24
    m=0.07342*10**24
    
    return (-G*M*m*x[1]/((x[1]*x[1]+x[3]*x[3])**(3/2))), x[0],(-G*M*m*x[3]/((x[1]*x[1]+x[3]*x[3])**(3/2))), x[2]

def gradient(x,t):
    
    return [[t,0,t,0],[0,1,0,1]]

t=arange(0,365*24*60*60)

x0_0=0
x1_0=400000000
y0_0=29000000
y1_0=0

x0=[x0_0,x1_0,y0_0,y1_0]

x=odeint(central, x0, t, Dfun=gradient)

time=time.time()-start_time
print "runing time ="+str(time)