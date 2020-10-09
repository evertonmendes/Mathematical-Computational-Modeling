# -*- coding: utf-8 -*-
#Nome: Éverton Luís Mendes da Silva
#N°USP: 10728171

import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D
#importing my files with the minimization methods
from DescentGrad import DescentGradient
from RandomS import RandomSearch
from SimulateAnnel import SimulateAnneling
from Calculation import Average, StandardDeviation
#For the Simulated Annealing
import time
import random
import math
#importing this class to get the necessary images
from Plot import Figures






'''-----------  This is main file to get the images of the project  --------------'''

# EQUATION 1
'''
ProjectTwoA=Figures(Equation='1')


ProjectTwoA.LevelCurves()
record1=ProjectTwoA.PlotDescent(xo=-3,yo=3, Steps=400)
average1=Average(record1)
standard_deviation1=StandardDeviation(record1)
print(average1, standard_deviation1)

record2=ProjectTwoA.PlotRandom(400)
average2=Average(record2)
standard_deviation2=StandardDeviation(record1)
print(average2, standard_deviation2)


ProjectTwoA.ComparisingOne(2,2)
ProjectTwoA.ComparisingOne(-2,1)
ProjectTwoA.ComparisingOne(3,-3.2)
ProjectTwoA.ComparisingOne(1,-2)
ProjectTwoA.ComparisingOne(0, 3)

'''
'''
plt.title('Points')
plt.xlabel('X')
plt.ylabel('Y')
plt.scatter(2,2, label='A(2,2)', color='red', marker='s')
plt.scatter(-2,1, label='B(-2,1)', color='blue', marker='s')
plt.scatter(3,-3.2, label='C(3,-3.2)', color='green', marker='s')
plt.scatter(1,-2, label='D(1,-2)', color='orange', marker='s')
plt.scatter(0, 3, label='E(0,3)', color='black', marker='s')
plt.legend()
plt.show()
'''
# EQUATION 2

#ProjectTwoB=Figures(Equation='2')
#ProjectTwoB.LevelCurves()
#ProjectTwoB.Surface_field3D()
#ProjectTwoB.PlotDescent(xo=2,yo=1)
#ProjectTwoB.PlotAnneling()

#ProjectTwoB.ComparisingTwo()
#ProjectTwoB.ComparisingTwo()
