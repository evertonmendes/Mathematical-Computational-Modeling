# -*- coding: utf-8 -*-
#Nome: Éverton Luís Mendes da Silva
#N°USP: 10728171

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from Data import GetDatasets
from OLS import LLS
import numpy as np
import matplotlib.patches as mpatches


#importing Data with the function GetDatasets

Boston, Cancer, California = GetDatasets()

mixBoston= Boston[0]
boston_features= Boston[1]

mixCancer= Cancer[0]
cancer_features= Cancer[1]

mixCalifornia= California[0]
california_features= California[1]




#2D PLOTS

class PlotDataset():

    def __init__(self, xName='', yName='',zName='', equation='',samples=[]):

        self.xName=xName
        self.yName=yName
        self.zName=zName
        self.equation=equation
        self.samples=samples
        

    def Plot2D(self):

        x=self.samples[self.xName].tolist()  
        y=self.samples[self.yName].tolist()
        #function LLS on the dataset
        P=LLS(x, y, errorfunction=self.equation)




        #constant that wiil be used on the minimization method (functions are in PDF Project)
        if(self.equation=='linear'):
            a0=P[0]
            a1=P[1]
        elif(self.equation=='quadratic'):
            a0=P[0]
            a1=P[1]
            a2=P[2]
        elif(self.equation=='cubic'):
            a0=P[0]
            a1=P[1]
            a2=P[2]
            a3=P[3]
        
        #style of the plot
        plt.title(self.xName+' x '+ self.yName)
        plt.xlabel(self.xName)
        plt.ylabel(self.yName)
        if(self.equation=='linear'):
            red_patch= mpatches.Patch(color='red', label='LLS')
        elif(self.equation=='quadratic'):
            red_patch= mpatches.Patch(color='red', label='LLS')
        elif(self.equation=='cubic'):
            red_patch= mpatches.Patch(color='red', label='LLS')
            
        
        plt.legend(handles=[red_patch])


        #ploting the real points
        plt.scatter(x, y, marker='.', alpha=0.5, color='black')

        
        if(self.equation=='linear'):
            
            minX=min(x)
            maxX=max(x)

            xlin=np.linspace(minX, maxX, 1000)

            ylin=[]
            for i in xlin:
                ys=a0+a1*i
                ylin.append(ys)
            #c=yequation1.getA1()

            plt.plot(xlin, ylin, LineWidth=1.2, color='red')
        
        elif(self.equation=='quadratic'):
            minX=min(x)
            maxX=max(x)
            xlin=np.linspace(minX, maxX, 1000)

            ylin=[]
            for i in xlin:
                ys=(a0)+(a1)*i+a2*(i**2)
                ylin.append(ys)

            
            plt.plot(xlin, ylin, LineWidth=1.2, color='red')

            
        elif(self.equation=='cubic'):
            minX=min(x)
            maxX=max(x)
            xlin=np.linspace(minX, maxX, 1000)

            ylin=[]
            for i in xlin:
                ys=(a0)+(a1)*i+a2*(i**2)+a3*(i**3)
                ylin.append(ys)
            
            plt.plot(xlin, ylin, LineWidth=1.2, color='red')
            
           
        plt.show()
        #print(P)



    def Plot3D(self):


            

        x=self.samples[self.xName].tolist()
        y=self.samples[self.yName].tolist()
        z=self.samples[self.zName].tolist()

        xmin=min(x)
        xmax=max(x)
        ymin=min(y)
        ymax=max(y)

            

        if(self.equation=='surfacePlane'):

            P=LLS(x, y, z, errorfunction=self.equation)
                
            a0=P[0]
            a1=P[1]
            a2=P[2]
        
            xlin=np.linspace(xmin, xmax, 1000)
            ylin=np.linspace(ymin, ymax, 1000)
            xlin, ylin = np.meshgrid(xlin, ylin)
            zlin=a0+a1*xlin+a2*ylin


        elif(self.equation=='surfaceQuadratic'):

            P=LLS(x, y, z, errorfunction=self.equation)

            a0=P[0]
            a1=P[1]
            a2=P[4]
            a3=P[3]
            a4=P[5]
            a5=P[2]
            

            xlin=np.linspace(xmin, xmax, 1000)
            ylin=np.linspace(ymin, ymax, 1000)

            xlin, ylin = np.meshgrid(xlin, ylin)
            zlin=a0 +a1*xlin + a2*ylin + a3*xlin*ylin+ a4*(xlin**2) + a5*(ylin**2)

            #print(zlin.shape)

        fig=plt.figure()
        ax=Axes3D(fig)
        ax.set_title('PLOTs 3D')
        ax.set_xlabel(self.xName)
        ax.set_ylabel(self.yName)
        ax.set_zlabel(self.zName)
        ax.scatter3D(x, y, z, marker='.',color='black', alpha=0.01, label='Real points')
        ax.plot_surface(xlin, ylin, zlin, color='blue', alpha=0.3, label='LLS')
        plt.show()

        #print(P)
    





#------------ 2D PLOTS ----------

'''
SC2D=PlotDataset('mean radius', 'mean perimeter', equation='linear', samples=mixCancer)
SB2D=PlotDataset('LSTAT', 'RM', equation='linear', samples=mixBoston)
SCa2D=PlotDataset('AveRooms', 'AveBedrms', equation='linear', samples=mixCalifornia)

#linear plots
SC2D.Plot2D()
SB2D.Plot2D()
SCa2D.Plot2D()


SC2D.yName='mean area'
SC2D.equation='quadratic'

SB2D.xName='MEDV'
SB2D.yName='LSTAT'
SB2D.equation='quadratic'

SCa2D.xName='MedHouseVal'
SCa2D.yName='Latitude'
SCa2D.equation='quadratic'

# quadratic plots
SC2D.Plot2D()
SB2D.Plot2D()
SCa2D.Plot2D()



SB2D.equation='cubic'
SC2D.equation='cubic'
SCa2D.equation='cubic'

# cubic plots
SC2D.Plot2D()
SB2D.Plot2D()
SCa2D.Plot2D()
'''

#---------------- 3D PLOTS
 
#SC3D=PlotDataset('mean radius', 'mean concavity', 'mean compactness', 'surfacePlane', mixCancer)
#SB3D=PlotDataset('RM', 'LSTAT', 'MEDV', 'surfacePlane', mixBoston)
#SCa3D=PlotDataset('Longitude', 'Latitude', 'Population', 'surfacePlane', mixCalifornia)

#SC3D.Plot3D()
#SB3D.Plot3D()
#SCa3D.Plot3D()

#SC3D.equation='surfaceQuadratic'
#SB3D.equation='surfaceQuadratic'
#SCa3D.equation='surfaceQuadratic'

#SC3D.Plot3D()
#SB3D.Plot3D()
#SCa3D.Plot3D()








#RM MEDV  LSTAT RM
#MEDV LSTAT
#RM, LSTAT, MEDV

#mean radius, mean perimeter
#mean radius, mean area
#mean radius, mean concavity, mean compactness


#AveRooms, AveBedrms
#MedHouseVal Latitude
#Longitude, Latitude, Block Population

        




