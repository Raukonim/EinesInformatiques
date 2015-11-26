# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 09:43:19 2015

@author: albert
"""

from __future__ import division, print_function
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
    M=6*10**24
    m=419450
    
    return (-G*M*x[1]/((x[1]**2+x[3]**2)**(3/2))), x[0],(-G*M*x[3]/((x[1]**2+x[3]**2)**(3/2))), x[2]

orb=100*60
t=linspace(0,orb,orb*1000)

vx_0=7660
x_0=0        
vy_0=0
y_0=412500+6400000

x0=[vx_0,x_0,vy_0,y_0]

x=odeint(central, x0, t)#, Dfun=gradient)

figure()
subplot(4,1,1)
title("Forces Centrals")
xlabel('temps')
ylabel('x')
plot(t,x[:,1])

#figure()
subplot(4,1,2)
xlabel('temps')
ylabel('y')
plot(t,x[:,3])

#figure()
subplot(4,1,3)
xlabel('temps')
ylabel('vx')
plot(t,x[:,0])

#figure()
subplot(4,1,4)
xlabel('temps')
ylabel('vy')
plot(t,x[:,2])

figure()
#subplot(5,1,5)
xlabel('x')
ylabel('y')
plot(x[:,1],x[:,3])
autoscale()
fig=gcf()
terra=Circle((0,0),6400000, color='b')
fig.gca().add_artist(terra)

#axis([-8000000, 8000000, -8000000, 8000000])

time=time.time()-start_time
print("runing time ="+str(time))