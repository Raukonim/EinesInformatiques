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

#%% Quadrat i Serra
t =linspace(0, 1, 500)
f =linspace(-250,250,500)
quadrat=square(2*pi*5*t)
fftQuadrat=fftshift(fft(quadrat))
pasBaixQ=abs(f)<=7
fftFiltQ=pasBaixQ*fftQuadrat
filtQuadrat=ifft(fftshift(fftFiltQ))

serra=sawtooth(2*pi*5*t)
fftSerra=fftshift(fft(serra))
pasBaixS=abs(f)<=6
fftFiltS=pasBaixS*fftSerra
filtSerra=ifft(fftshift(fftFiltS))


figure(1)
subplot(411)
plot(t, quadrat)
ylim(0,1.2)
subplot(412)
plot(f, abs(fftQuadrat))
subplot(413)
plot(f, abs(fftFiltQ))
#xlim(0,20)
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
plot(f, abs(fftFiltS))
#xlim(0,20)
xlabel("Hz")
subplot(414)
plot(t,real(filtSerra))

#%% Audio
N,audio=read('cello.wav')
L=1


audio=audio[audio!=0]
mida=audio.shape
dades=audio[:N]
x=linspace(-N/(2*L),N/(2*L),N)

fftdades=fftshift(fft(dades))

figure(3)
subplot(211)
plot(dades)
subplot(212)
plot(x, abs(fftdades))
interactive(False)

for i in range(9):
    segon=fftshift(fft(audio[i*N:i*N+N]))
    #Ñprint(i*N, i*N+N)
    figure()
    semilogy(x,abs(segon))
    xlim(-22500,22500)
    if len(str(i))==1:
        h='0'+str(i)
    else:
        h=str(i)
    savefig('sample'+h+'.png')
