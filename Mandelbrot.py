# -*- coding: utf-8 -*-
"""
Created on Mon Nov 09 10:48:45 2015

@author: a.fajula
"""

from __future__ import division
from pylab import*

interactive(True)
close('all')

M=1000
top=2
z=zeros([M,M])
re=linspace(-2,1,M)
im=linspace(-1.5,1.5,M)
X, Y=meshgrid(re,im)
c=X+1j*Y

cm=double(zeros([M,M]))
cmsuma=double(zeros([M,M]))
figure(0)
j=0
for i in range(0,90,10):
    j=1+i/10
    #print j
    z=(z*z)+c
    cm=(abs(z)<top)
    subplot(3,3,j)
    title(i)
    axis('off')
    imshow(cm, cmap='gray')

zs=zeros([M,M])
for i in range(0,90):
    zs=(zs*zs)+c
    #zs=array([2 for m in range(M) for n in range(M) if abs(zs[m,n])>2])
    '''for j in range(M):
        for n in range(M):
            if abs(zs[j,n])>top:
                zs[j,n]=2
                '''
    k=(abs(zs)<top)
    cmsuma=cmsuma+k

figure(1)
axis('off')
imshow(cmsuma, cmap='prism')
'''
figure()
imshow(abs(c)+angle(c))
'''