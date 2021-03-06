# -*- coding: utf-8 -*-
"""
Created on Mon Nov 09 10:48:45 2015

@author: a.fajula
"""

from __future__ import division
from pylab import *
import time
import os

start_time = time.time()


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

zs=zeros([M,M])
for i in range(0,90):
    zs=(zs*zs)+c
    #zs=nan_to_num(zs)
    zs[abs(zs)>top]=top
    k=(abs(zs)<top)
    cmsuma=cmsuma+k
    if i%10==0:
            j=1+i/10
            #print j
            z=(z*z)+c
            cm=(abs(z)<top)
            subplot(3,3,j)
            title(i)
            axis('off')
            imshow(cm, cmap='gray')
    '''if len(str(i))==1:
        h='0'+str(i)
    else:
        h=str(i)
    imsave('cmsuma'+h+'.png', cmsuma, cmap='prism')

os.system('convert.im6 -delay 50 -loop 0 *.png mandelbrot.gif')
os.system('rm *.png')'''

figure(1)
axis('off')
imshow(cmsuma, cmap='prism')
#imsave('mandelbrot90.png', cmsuma, cmap='prism')
'''
figure()
imshow(abs(c)+angle(c))
'''
#writeGif()
time=time.time()-start_time
print "runing time ="+str(time)