import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D

'''
t=np.linspace(0, 4, 200)


print(t)


for i in range(2):

    print(i)
'''

'''
for i in [200, 300, 400, 500, 1000, 2000]:


    t=np.linspace(0, 4, i)
    plt.plot(t, np.cos(220*t)) 
    plt.show()

'''



signal=[]
t=np.linspace(0,1, 1000)
signal1=[]

for j in t:

    sum_cosines=0.0
    sum_sines=0.0

    for i in [50, 150.8]:

        #print(i, j)
        argument=2*(np.pi)*i*j
        element=np.cos(argument)
        element1=np.sin(argument)
        sum_sines+=float(element1)
        print(element)
        sum_cosines+=float(element)
        #print(sum_cosines)


    #print(len(sum_cosines[0]))
    signal.append(sum_cosines)
    signal1.append(sum_sines)

print(signal)

#for i in range(len(signal)):
    
#    signal[i]=signal[i].real
plt.plot(signal, signal1)
plt.show()


fourier=np.fft.fft(signal)
#fourier=fourier*fourier
w=np.fft.fftfreq(len(signal))



real1=[]
imag1=[]
for k in fourier:

    i=np.real(k)
    j=np.imag(k)

    #i=float(i)
    #j=float(j)
    real1.append(i)
    imag1.append(j)

#n = len(signal1)
#timestep = 0.1
#ffreq = np.fft.fftfreq(n, d=timestep)
plt.plot(t, signal)
plt.show()

resignal=np.fft.ifft(fourier)
plt.plot(t, resignal)
plt.show()


fig=plt.figure()
ax=Axes3D(fig)
ax.plot(signal, signal1, t)
plt.show()