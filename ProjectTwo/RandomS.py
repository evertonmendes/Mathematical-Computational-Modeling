# -*- coding: utf-8 -*-
#Nome: Éverton Luís Mendes da Silva
#N°USP: 10728171

from random import randint
import numpy as np


# function that Make a random Search in Npoints (searching for minimum)
def RandomSearch(Xmin, Xmax, Ymin, Ymax, Npoints, equation):

    #RandomPoints=[]
    xPoint=[]
    yPoint=[]
    minimum=[]
    recordMinimum=[]


    for i in range(Npoints):
        
        xRandom=0.00001*randint(Xmin*(10**5), Xmax*(10**5))
        yRandom=0.00001*randint(Ymin*(10**5), Ymax*(10**5))
        #RandomPoints.append([xRandom, yRandom])
        xPoint.append(xRandom)
        yPoint.append(yRandom)


        if equation=='1':
            
            Zo=xRandom**2+yRandom**2
            minimum.append(Zo)            
                
        elif equation=='2':
                
            Zo= (-1)*(np.e)**((-1)*((xRandom-1)**2+yRandom**2)/(0.3*0.3)) -5*((np.e)**((-16)*((xRandom-2)**2+(yRandom-2)**2)))
            minimum.append(Zo)
        
        recordMinimum.append(min(minimum))
        



    #index of the point with minimum value in Points
    Index_min=minimum.index(min(minimum))
    Points=[xPoint, yPoint]

    return Points, Index_min, recordMinimum










