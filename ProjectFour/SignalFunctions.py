#Name: Éverton Luís Mendes da Silva
#N USP: 10728171



import matplotlib.pyplot as plt
import numpy as np
import scipy as scy
from scipy.signal import butter, filtfilt
from scipy.ndimage import gaussian_filter


#function that returns a signal which is the sum of several cosines 
def SignalCosine(m, freq, time=2, H=4):

    '''
    m, function to modulate the cosines
    freq, fundamental frequence of the signal(Hz)
    time, 0<t<time for the signal 
    H, number of harmonic partials
    '''

    signal=[]
    signal1=[]
    t=np.linspace(0,time, 2000)
    
    Hlist=[]
    for i in range(H):
        Hlist.append(i+1)

    for j in t:
        sum_cosines=0.0
        sum_sines=0.0

        for i in Hlist:

            argument=2*(np.pi)*freq*i*j

            element=np.cos(argument)
            element1=np.sin(argument)

            sum_sines+=float(element1)
            sum_cosines+=float(element)
   
        sum_cosines= sum_cosines*(m(j))
        sum_sines= sum_sines*(m(j))

        signal.append(sum_cosines)
        signal1.append(sum_sines)

    return signal, signal1, t



def FourierTransform(data):

    
    fourier=np.fft.fft(data)
    #print(fourier)

    T=0.001
    f=np.fft.fftfreq(len(data), T)
    frequency= f[:len(data)//2]
    amplitude=np.abs(fourier)[:len(data)//2]


    return frequency, amplitude


def filter_lowpass(data, cutoff=20, fs=2000, order=2):

    '''
    data , array to be filtered
    cutoff, the frequency cut of the low pass
    fs, max size of the time
    order, order of the filter

    '''
    nyq=0.5*fs
    normal_cutoff=cutoff/nyq
    b, a= butter(order, normal_cutoff, btype='low')
    y=filtfilt(b, a, data)

    return y


def filter_highpass(data, cutoff=20, fs=2000, order=5):

    nyq=0.5*fs
    normal_cutoff=cutoff/nyq
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    y = filtfilt(b, a, data)
    
    return y


def filter_bandpass(data, lowcut=20, highcut=35, fs=2000, order=2):

    nyq=0.5*fs
    low= lowcut/nyq
    high= highcut/nyq

    b, a = butter(order, [low, high], 'bandpass', analog=False)
    y=filtfilt(b, a, data)


    return y



def filter_gaussian(data, sigma=7):

    y=gaussian_filter(data, sigma)


    return y

