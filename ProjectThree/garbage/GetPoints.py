import matplotlib.pyplot as plt
import numpy as np
from EulerMethod import odeEuler




t1 = np.linspace(0,2,21)
y_true = np.exp(t1)
plt.plot(t1, y_true, 'r-')



click_points = plt.ginput(3)
print(click_points)



for Axis_point in click_points:

    
    print(Axis_point[1])
    y1 = Axis_point[1]
    f = lambda y,t: y
    y = odeEuler(fx=f,fy=f,y0=y1,x0=y1,t=t1)
    plt.plot(t1,y)
    #plt.legend(['Euler','True'])


plt.plot(t1, t1*t1)
plt.show()

#click_points=[]




'''
for Axis_point in click_points:


    x1=Axis_point[0]
    x2=Axis_point[1]
    f1= lambda x,y,t: x-x*y 
    f2= lambda x,y,t: -y+xy
    xt,yt=odeEuler(fx=f1,fy=f2,x0=x1,y0=x2,t=t1,System_type='2')
'''

plt.show() 

    
