# -*- coding: utf-8 -*-
"""
Created on Fri Nov 06 14:29:21 2015

@author: a.fajula
"""

from __future__ import division
from pylab import*
from scipy.integrate import quad
from scipy.integrate import simps

interactive(True)
close('all')

err=0.1
ermin=10**-15
pas=0
error=array([])
itera=array([])
k=0
while(abs(err)>ermin):
    
    pas=pas+((1/16**k)*((4/(8*k+1))-(2/(8*k+4))-(1/(8*k+5))-(1/(8*k+6))))
    err=pi-pas
    error=append(error, err)
    itera=append(itera, k)
    
    k+=1

bbp=pas

figure('BBP:'+ str(bbp))
plot(itera, error)


iteraRandom=array([])
errRandom=array([])
interns=0
for i in range(0,10000):
    dades=2*random_sample([2])-1
    #interns=0
    if(sqrt(((dades[0]*dades[0])+(dades[1]*dades[1])))<=1):interns+=1
    iterac=i+1
    iteraRandom=append(iteraRandom, iterac)
    quoc=interns/iterac*4
    #print quoc
    err=pi-quoc
    errRandom=append(errRandom, err)

randomPi=quoc

figure('Random:'+ str(randomPi))
plot(iteraRandom, errRandom)


f1=lambda x: exp(-(x*x))
f2=lambda x: 1/(1-(x*x))

quad1, errq1=quad(f1, -inf, inf)
quad1Pi=quad1*quad1
quad2, errq2=quad(f2, 0.0001, inf)
quad2Pi=2*quad2

x=linspace(0.000001, 10000, 100000)
y1=exp(-(x*x))
y2=1/(1-(x*x))
simps1=simps(y1)
simps1Pi=2*simps1*simps1
simps2=simps(y2)
simp2Pi=2*simps2