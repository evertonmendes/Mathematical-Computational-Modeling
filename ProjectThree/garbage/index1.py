import numpy as np
from matplotlib import pyplot as plt
from EulerMethod import odeEuler

# Differential equation
# diff = y'= y/x (or say x+y)
def diff(x,y):
    return  y# try also x+y

x = np.linspace(-4,4,30)
y = np.linspace(-4,4,30)

# use x,y
for j in x:
    for k in y:
        slope = diff(j,k)
        domain = np.linspace(j-0.07,j+0.07,2)
        def fun(x1,y1):
            z = slope*(domain-x1)+y1
            return z

        listDomain=[]
        listfun=[]
        plt.plot(domain,fun(j,k),solid_capstyle='projecting',solid_joinstyle='bevel')

plt.title("Slope field y")
plt.grid(True)

tt = np.linspace(0,2,21)
yo = 0.3
f = lambda y,t: y
y = odeEuler(fx=f,fy=f,x0=yo,y0=yo,t=tt, System_type='1')
y_true = np.exp(tt)
plt.plot(tt,y,'b.-',tt,y_true,'r-')
plt.legend(['Euler','True'])
#plt.axis([0,2,0,9])
#plt.grid(True)
#plt.title("Solution of $y'=y , y(0)=1$")
#plt.show()


plt.show()
    
print("End of the program")