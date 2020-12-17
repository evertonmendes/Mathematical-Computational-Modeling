#Name: Éverton Luís Mendes da Silva
#N USP: 10728171



import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D





def UsualPlot(x, y, type='0'):


    plt.xlabel('t')
    plt.ylabel('signal(t)')

    if (type=='1'):

        plt.title('Signal')
        plt.plot(x, y, label='low pass')

    elif(type=='2'):

        plt.title('Signal')
        plt.plot(x, y, label='high pass')
    
    elif(type=='3'):

        plt.title('Signal')
        plt.plot(x, y, label='band pass')

    elif(type=='4'):

        plt.title('Signal')
        plt.plot(x, y, label='gaussian pass')

    elif(type=='0'):

        plt.title('Signal')
        plt.plot(x, y)

    elif(type=='5'):

        plt.title('FFT')
        plt.plot(x, y, label='Fourier')
        plt.xlabel('Freq')
        plt.ylabel('Mod')


    
    
    plt.legend()
    plt.show()



def LisajousPlot(x, y):


    plt.title('Lisajous Plot')
    plt.xlabel('Real')
    plt.ylabel('Imag')
    plt.plot(x, y)
    plt.show()


def Lisajous3D(x, y, z):


    fig=plt.figure()
    ax=Axes3D(fig)
    ax.set_title('3D PLOT')
    ax.set_xlabel('Real')
    ax.set_ylabel('Imag')
    ax.set_zlabel('t')
    ax.plot(x, y, z, color='Red')
    plt.show()


def FilterPlot(t, y1, y2, y3):


    plt.title('Signal')
    plt.xlabel('t')
    plt.ylabel('signal(t)')


    plt.plot(t, y1, label='lowpass')
    plt.plot(t, y2, label='highpass')
    plt.plot(t, y3, label='bandpass')

    plt.legend()
    plt.show()



    



