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

def eqdif1(y,t):
    """
    y[0]=velocitat
    y[1]=angle
    y[2]=temps
    """
    g=9.8
    L=10
    m=1
    b=0
    omega=0
    amp=0
    
    return  (-g*sin(y[1])/L)+(-b*y[0]+amp*cos(omega*t)/(m*L*L)), y[0]

def eqdif2(y,t):
    """
    y[0]=velocitat
    y[1]=angle
    y[2]=temps
    """
    g=9.8
    L=10
    m=1
    b=0.3
    omega=0
    amp=0
    
    return  (-g*sin(y[1])/L)+(-b*y[0]+amp*cos(omega*t)/(m*L*L)), y[0]

def eqdif3(y,t):
    """
    y[0]=velocitat
    y[1]=angle
    y[2]=temps
    """
    g=9.8
    L=1
    m=1
    b=0.5
    omega=0.666
    amp=1.35
    
    return  (-g*sin(y[1])/L)+(-b*y[0]+amp*cos(omega*t)/(m*L*L)), y[0]

t=arange(0,60,0.1)
y0_0 = 0
y1_0 = 1
y0=[y0_0, y1_0]

y1=odeint(eqdif1, y0, t)
y2=odeint(eqdif2, y0, t)
y3=odeint(eqdif3, y0, t)

def plots(y, t, titol):
    figure()
    subplot(2,1,1)
    title(titol)
    xlabel('temps')
    ylabel('Omega')
    grid(axis='y')
    plot(t,y[:,0])
    
    subplot(2,1,2)
    xlabel('temps')
    ylabel('Theta')
    grid(axis='y')
    plot(t,y[:,1])


plots(y1,t,'Harmonic Oscillator')
plots(y2,t,'Damped Harmonic Oscillator')
plots(y3,t,'Driven Damped Harmonic Oscillator')

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
title("Central Forces")
xlabel('temps')
ylabel('x')
grid(axis='y')
plot(t,x[:,1])
ticklabel_format(style='sci', axis='y', scilimits=(0,0))

#figure()
subplot(4,1,2)
xlabel('temps')
ylabel('y')
grid(axis='y')
plot(t,x[:,3])
ticklabel_format(style='sci', axis='y', scilimits=(0,0))

#figure()
subplot(4,1,3)
xlabel('temps')
ylabel('vx')
grid(axis='y')
plot(t,x[:,0])
ticklabel_format(style='sci', axis='y', scilimits=(0,0))

#figure()
subplot(4,1,4)
xlabel('temps')
ylabel('vy')
grid(axis='y')
plot(t,x[:,2])
ticklabel_format(style='sci', axis='y', scilimits=(0,0))

figure()
#subplot(5,1,5)
title('ISS orviting Earth ')
xlabel('x')
ylabel('y')
plot(x[:,1],x[:,3], 'r')
ticklabel_format(style='sci', axis='both', scilimits=(0,0))
axis('equal')
fig=gcf()
terra=Circle((0,0),6400000, color='b')
fig.gca().add_artist(terra)

#axis([-8000000, 8000000, -8000000, 8000000])

time=time.time()-start_time
print("runing time ="+str(time))