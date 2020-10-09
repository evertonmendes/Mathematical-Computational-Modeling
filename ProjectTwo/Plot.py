# -*- coding: utf-8 -*-
#Nome: Éverton Luís Mendes da Silva
#N°USP: 10728171



import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from DescentGrad import DescentGradient
from RandomS import RandomSearch
from SimulateAnnel import SimulateAnneling
from Calculation import Average, StandardDeviation



class Figures():

    def __init__(self, xmin=-4, xmax=4, ymin=-4, ymax=4, Equation='1'):
        self.xmin=xmin
        self.xmax=xmax
        self.ymin=ymin
        self.ymax=ymax
        self.Equation=Equation

    #Plot the Level Curves of the Scalar Field
    def LevelCurves (self):

        X=np.arange(-4, 4, 0.1)
        Y=np.arange(-4, 4, 0.1)
        X, Y= np.meshgrid(X, Y)

        plt.title('Scalar Field')
        if self.Equation=='1':
            Z=X**2+Y**2
        elif self.Equation=='2':
            Z= (-1)*(np.e)**((-1)*((X-1)**2+Y**2)/(0.3*0.3)) -5*((np.e)**((-16)*((X-2)**2+(Y-2)**2)))
        plt.contourf(X, Y, Z)
        plt.contour(X, Y, Z, colors = 'k', linewidths = 1, linestyles = 'solid', alpha=0.7)
        plt.show()


    #Plot Three Grafics about Gradient Descent; (1)'Scalar Field', (2)'Gradient', (3)'Scalar Field and Gradient' (4)'Gradient Descent' 
    def PlotDescent (self, xo, yo, Steps=200, Delta=-0.4, Alpha=0.9):

        X=np.arange(-4, 4, 0.1)
        Y=np.arange(-4, 4, 0.1)
        X, Y= np.meshgrid(X, Y)
        Points, record=DescentGradient(xo, yo, self.Equation, Delta, Alpha, Steps)

        if self.Equation=='1':
            Z=X**2+Y**2
        elif self.Equation=='2':
            Z= (-1)*(np.e)**((-1)*((X-1)**2+Y**2)/(0.3*0.3)) -5*((np.e)**((-16)*((X-2)**2+(Y-2)**2)))


        plt.title('Gradient')
        gradx, grady = np.gradient (Z, 0.1, 0.1)
        plt.quiver(X, Y, gradx , grady, scale=150, alpha=0.6, label='Vectors')
        plt.legend()
        plt.show()


        plt.title('Scalar field and Gradient')
        
        plt.contourf(X, Y, Z)
        #plt.pcolormesh(X, Y, Z, cmap = cm.autumn, alpha=1)
        plt.contour(X, Y, Z, colors = 'k', linewidths = 1, linestyles = 'solid', alpha=0.7)
        plt.quiver(X, Y, gradx , grady, scale=150,  alpha=0.6, label= 'Vectors')
        plt.show()


        plt.title('Gradient Descent')
        plt.quiver(X, Y, gradx , grady, scale=150, alpha=0.6, label='Vectors')
        plt.scatter(Points[0], Points[1], color='red', marker='.', label='Points')
        plt.legend()
        plt.show()

        plt.title('Minimum')

        return record
    
    def PlotRandom (self, N_iterations):

        List_Points, Min, record= RandomSearch(self.xmin, self.xmax, self.ymin, self.ymax, N_iterations, self.Equation)

        plt.title('Random Search')
        plt.scatter(List_Points[0], List_Points[1], label='Random Points', color='black', alpha=0.7, marker='.')
        plt.plot(List_Points[0][Min], List_Points[1][Min], color='red', marker='s', label='Minimum Point')
        plt.legend()
        plt.show()

        return record


    def PlotAnneling (self):

        recordPoints=SimulateAnneling()
        plt.title('Simulate Anneling')
        plt.xlabel('STEP')
        plt.ylabel('Scalar Value')
        plt.plot(recordPoints, label='Minimum')
        plt.legend()
        plt.show()


    def Surface_field3D(self):

        X=np.arange(-4, 4, 0.1)
        Y=np.arange(-4, 4, 0.1)
        X, Y= np.meshgrid(X, Y)
        if self.Equation=='1':
            Z=X**2+Y**2
        elif self.Equation=='2':
            Z= (-1)*(np.e)**((-1)*((X-1)**2+Y**2)/(0.3*0.3)) -5*((np.e)**((-16)*((X-2)**2+(Y-2)**2)))
        fig=plt.figure()
        ax=Axes3D(fig)
        ax.set_title('Surface')
        ax.plot_surface(X, Y, Z, color='blue', alpha=1, label='Scalar Field')
        ax.set_label('Scalar Field')
        plt.show()

    #function that plot de Minimum curves of an array
    def MinimumPlot(self, List=[]):

        plt.title('Steps x Minimum')
        plt.xlabel('Steps')
        plt.ylabel('Minimum')

        #gettig the average and the Standard Deviation
        average=Average(List)
        standard_deviation=StandardDeviation(List)

        plt.plot(List, color='blue', label='Average= '+str(round(average, 4))+', Deviation= '+str(round(standard_deviation, 4)))
        plt.legend()
        plt.show()

        return average, standard_deviation

    def ComparisingOne(self, xi, yi):

        #Gradient Descent
        Points1, record1=DescentGradient(xi, yi, self.Equation, delta=-0.4, alpha=0.9, steps=200)
        #Random Search
        Points2, index_m, record2= RandomSearch(Xmin=self.xmin, Xmax=self.xmax, Ymin=self.ymin, Ymax=self.ymax, Npoints=200, equation=self.Equation)

        print('Gradient Descent')
        self.MinimumPlot(record1)
        print('Random Search')
        self.MinimumPlot(record2)


    def ComparisingTwo(self):

        #Simulated Annealing
        record1=SimulateAnneling()
        #RandomSearch
        Points2, index_min, record2=RandomSearch(Xmin=self.xmin, Xmax=self.xmax, Ymin=self.ymin, Ymax=self.ymax, Npoints=600, equation=self.Equation)

        print('Simulated Annealing')
        self.MinimumPlot(record1)
        print('Random Search')
        self.MinimumPlot(record2)












        









#Pedro=Figures(Equation='2')
#Pedro.ComparisingTwo()





    






'''

plt.scatter(NewPoints[0], NewPoints[1], color='red', marker='.')
#plt.contourf(X, Y, Z, n=[0,2,4,6])
#plt.contour(X, Y, Z, colors = 'k', linewidths = 1, linestyles = 'solid', alpha=0.5)
plt.quiver(X, Y, gradx , grady, scale=800, linestyles= '-', linewidths=1, alpha=0.6)
plt.show()

'''

















'''
x = np.linspace(-5, 5, 1000) 
y = np.linspace(-5, 5, 1000) 
X, Y = np.meshgrid(x, y, sparse=True) 

#Z=(np.e)**(-((X-1)**2+Y**2))+(np.e)**(-(X**2+Y**2+2))
Z= (-1)*(np.e)**((-1)*((X-1)**2+Y**2)/(0.3*0.3)) -5*((np.e)**((-16)*((X-2)**2+(Y-2)**2)))
#print(Z)
plt.pcolormesh(X, Y, Z, cmap = cm.autumn, alpha=1) 
plt.contour(x,y,Z, color='k')
plt.show()



fig=plt.figure()
ax=Axes3D(fig)
ax.plot_surface(X, Y, Z, color='blue', alpha=1)
plt.show()
'''


