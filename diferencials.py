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



time=time.time()-start_time
print "runing time ="+str(time)