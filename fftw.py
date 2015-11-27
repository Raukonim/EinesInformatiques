# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 11:27:34 2015

@author: albert
"""

from __future__ import division, print_function
from pylab import*
from scipy.signal import square, sawtooth
import time

from scipy.io.wavfile import read, write

start_time = time.time()

interactive(True)
close('All')

N,audio=read('cello.wav')
l=audio.shape
L=l[0]
x=uint16(linspace(-N/(2*L),N/(2*L)))

t =linspace(0, 1, 500)
f =linspace(-250,250,500)
quadrat=square(2*pi*5*t)
fftQuadrat=fftshift(fft(quadrat))
pasBaixQ=abs(f)<=7
fftFiltQ=pasBaixQ*fftQuadrat
filtQuadrat=ifft(fftFiltQ)

serra=sawtooth(2*pi*5*t)
fftSerra=fftshift(fft(serra))
pasBaixS=abs(f)<=6
fftFiltS=pasBaixS*fftSerra
filtSerra=ifft(fftFiltS)


figure(1)
subplot(411)
plot(t, quadrat)
ylim(0,1.2)
subplot(412)
plot(f, abs(fftQuadrat))
subplot(413)
plot(f[249:279], abs(fftFiltQ[249:279]))
xlim(0,20)
xlabel("Hz")
subplot(414)
plot(t,real(filtQuadrat))

figure(2)
subplot(411)
plot(t, serra)
ylim(0,1.2)
subplot(412)
plot(f, abs(fftSerra))
subplot(413)
plot(f[249:279], abs(fftFiltS[249:279]))
xlim(0,20)
xlabel("Hz")
subplot(414)
plot(t,real(filtSerra))