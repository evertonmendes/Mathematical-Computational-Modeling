#Name: Éverton Luís Mendes da Silva
#N USP: 10728171




import matplotlib.pyplot as plt
import numpy as np
import scipy as scy
from scipy.signal import butter, filtfilt
from scipy.ndimage import gaussian_filter
import math
from mpl_toolkits.mplot3d import Axes3D
from SignalFunctions import  SignalCosine, FourierTransform, filter_lowpass, filter_highpass, filter_bandpass, filter_gaussian
from PlotSignal import UsualPlot, LisajousPlot, Lisajous3D, FilterPlot


f1=lambda x: (np.e)**(-x)
f2=lambda x: x*x +(-1)*x*x*x
f3=lambda x: (x**2)+((-1)*(x**4))+(x)*(np.cos(x))


#signalA1cos, signalA1sin, tA1= SignalCosine(f1, 10)
#freqA1, ampA1=FourierTransform(signalA1cos)

#signalA2cos, signalA2sin, tA2= SignalCosine(f2, 10)
#freqA2, ampA2=FourierTransform(signalA2cos)

#signalA3cos, signalA3sin, tA3= SignalCosine(f3, 10)
#freqA3, ampA3=FourierTransform(signalA3cos)

#signalB1cos, signalB1sin, tB1= SignalCosine(f1, 25)
#freqB1, ampB1=FourierTransform(signalB1cos)

#signalB2cos, signalB2sin, tB2= SignalCosine(f2, 25)
#freqB2, ampB2=FourierTransform(signalB2cos)

#signalB3cos, signalB3sin, tB3= SignalCosine(f3, 25)
#freqB3, ampB3=FourierTransform(signalB3cos)




'''
UsualPlot(tA1, signalA1cos)
LisajousPlot(signalA1cos, signalA1sin)
Lisajous3D(signalA1cos, signalA1sin, tA1)
UsualPlot(freqA1, ampA1, '5')


UsualPlot(tA2, signalA2cos)
LisajousPlot(signalA2cos, signalA2sin)
Lisajous3D(signalA2cos, signalA2sin, tA2)
UsualPlot(freqA2, ampA2, '5')

UsualPlot(tA3, signalA3cos)
LisajousPlot(signalA3cos, signalA3sin)
Lisajous3D(signalA3cos, signalA3sin, tA3)
UsualPlot(freqA3, ampA3, '5')

UsualPlot(tB1, signalB1cos)
LisajousPlot(signalB1cos, signalB1sin)
Lisajous3D(signalB1cos, signalB1sin, tB1)
UsualPlot(freqB1, ampB1, '5')

UsualPlot(tB2, signalB2cos)
LisajousPlot(signalB2cos, signalB2sin)
Lisajous3D(signalB2cos, signalB2sin, tB2)
UsualPlot(freqB2, ampB2, '5')

UsualPlot(tB3, signalB3cos)
LisajousPlot(signalB3cos, signalB3sin)
Lisajous3D(signalB3cos, signalB3sin, tB3)
UsualPlot(freqB3, ampB3, '5')
'''

'''

y1A1=filter_lowpass(signalA1cos)
y2A1=filter_highpass(signalA1cos)
y3A1=filter_bandpass(signalA1cos)
y4A1=filter_gaussian(signalA1cos)

y1A2=filter_lowpass(signalA2cos)
y2A2=filter_highpass(signalA2cos)
y3A2=filter_bandpass(signalA2cos)
y4A2=filter_gaussian(signalA2cos)

y1A3=filter_lowpass(signalA3cos)
y2A3=filter_highpass(signalA3cos)
y3A3=filter_bandpass(signalA3cos)
y4A3=filter_gaussian(signalA3cos)


y1B1=filter_lowpass(signalB1cos)
y2B1=filter_highpass(signalB1cos)
y3B1=filter_bandpass(signalB1cos)
y4B1=filter_gaussian(signalB1cos)


y1B2=filter_lowpass(signalB2cos)
y2B2=filter_highpass(signalB2cos)
y3B2=filter_bandpass(signalB2cos)
y4B2=filter_gaussian(signalB2cos)


y1B3=filter_lowpass(signalB3cos)
y2B3=filter_highpass(signalB3cos)
y3B3=filter_bandpass(signalB3cos)
y4B3=filter_gaussian(signalB3cos)



FilterPlot(tA1, y1A1, y2A1, y3A1)
FilterPlot(tA2, y1A2, y2A2, y3A2)
FilterPlot(tA3, y1A3, y2A3, y3A3)
FilterPlot(tB1, y1B1, y2B1, y3B1)
FilterPlot(tB2, y1B2, y2B2, y3B2)
FilterPlot(tB3, y1B3, y2B3, y3B3)



UsualPlot(tA1, y4A1, '4')
UsualPlot(tA2, y4A2, '4')
UsualPlot(tA3, y4A3, '4')
UsualPlot(tB1, y4B1, '4')
UsualPlot(tB2, y4B2, '4')
UsualPlot(tB3, y4B3, '4')

'''

