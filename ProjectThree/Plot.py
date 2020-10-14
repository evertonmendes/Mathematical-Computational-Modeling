# -*- coding: utf-8 -*-
#Nome: Éverton Luís Mendes da Silva
#N°USP: 10728171


import matplotlib.pyplot as plt
import numpy as np
import math
import numpy as np
import matplotlib.pyplot as plt
from DirectionField import Direction_Field
from EulerMethod import odeEulerOne, odeEulerTwo



#create a diferential objetc that have some methods for visualization
class Plot_Dif_Eq():

    '''
    f1 - function of the right hand of a diferential equation
    xrange - [xmin, xmax] domain
    yrange - [ymin, ymax] domain
    Equation - Type of system, '1' one variable, '2' two variables
    
    '''


    def __init__(self, f1, xrange=[-2,2], yrange=[-2,2], Equation=''):

        self.f1=f1
        self.xrange=xrange
        self.yrange= yrange
        self.Equation= Equation


    #Plot The Direction Field of a ODE's
    def PlotDirection(self):

        if self.Equation=='2':

            x1, y1, dx1, dx2, m1= Direction_Field(f=self.f1, Ode_type=self.Equation, xran=self.xrange, yran=self.yrange)

            plt.title('Direction Field')
            plt.xlabel('x')
            plt.ylabel('y')

            
            plt.quiver(x1, y1, dx1, dx2, m1, pivot='mid', color='blue', alpha=0.9)       

            plt.show()

        elif self.Equation=='1':

            list_domain, list_fun= Direction_Field(f=self.f1, Ode_type=self.Equation, xran=self.xrange, yran=self.yrange)
        
            plt.title('Direction Field')
            plt.xlabel('t')
            plt.ylabel('x')

            for i in range(len(list_domain)):

                plt.plot(list_domain[i], list_fun[i],solid_capstyle='projecting',solid_joinstyle='bevel')

            plt.show()     


    #method that makes Euler solution after the user chosen a point
    def PlotEulerMethod(self):


        plt.title('Euler´s Method')
        plt.xlim(self.xrange)
        plt.ylim(self.yrange)

        if self.Equation=='1':

            list_domain, list_fun= Direction_Field(f=self.f1, Ode_type=self.Equation, xran=self.xrange, yran=self.yrange)

            for i in range(len(list_domain)):

                plt.plot(list_domain[i], list_fun[i],solid_capstyle='projecting',solid_joinstyle='bevel', color='black', alpha=0.8)

        elif self.Equation=='2':

            x1, y1, dx1, dy1, m1= Direction_Field(f=self.f1, Ode_type=self.Equation, xran=self.xrange, yran=self.yrange)

            plt.quiver(x1, y1, dx1, dy1, m1, pivot='mid', color='blue', alpha=0.9)



        #numbers of points to chose
        click_points=plt.ginput(3)


        if self.Equation=='1':

            plt.xlabel('t')
            plt.ylabel('x')

            for Axis_point in click_points:

                ta=np.linspace(Axis_point[0], self.xrange[1], 500)
                xa= odeEulerOne(fx=self.f1, x0= Axis_point[1], t=ta)
                plt.plot(ta, xa, label='Point= ('+str(round(Axis_point[0], 3))+', '+str(round(Axis_point[1], 3))+')')

          

        elif self.Equation=='2':

            plt.xlabel('x')
            plt.ylabel('y')


            for Axis_point in click_points:

                tb = np.linspace(0,30,3200)
                xb, yb= odeEulerTwo(R0=Axis_point[0], F0= Axis_point[1],alpha=1, beta=1, gamma=1, delta=1, t=tb)



                plt.plot(xb, yb, label='Point= ('+str(round(Axis_point[0], 3))+', '+str(round(Axis_point[1], 3))+')')


        plt.legend()
        plt.show()




