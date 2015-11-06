# -*- coding: utf-8 -*-
"""
Created on Fri Nov 06 14:29:21 2015

@author: a.fajula
"""

from __future__ import division
from pylab import*

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

figure('BBP')
plot(itera, error)


iteraRandom=array([])
errRandom=array([])

for i in range(0,10000,10):
    dades=random_sample([i,2])-0.5
    interns=0
    for j in range(i):
        x,y=dades[j,:]
        if(sqrt((x*x+y*y))<=1/2):interns+=1
    iterac=i+1
    iteraRandom=append(iteraRandom, iterac)
    quoc=interns/iterac
    print quoc
    err=pi-quoc
    errRandom=append(errRandom, err)

randomPi=quoc

figure('Random')
plot(iteraRandom, errRandom)