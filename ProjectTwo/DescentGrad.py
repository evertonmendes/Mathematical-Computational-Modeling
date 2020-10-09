# -*- coding: utf-8 -*-
#Nome: Éverton Luís Mendes da Silva
#N°USP: 10728171


import numpy as np
import matplotlib.pyplot as plt


#Descent Gradient of a scalar field
def DescentGradient(Xo=-2, Yo=-2, equation='1', delta=-0.4, alpha=0.85, steps=200):


    '''
    Xo initial x coordinate of a point
    Yo initial y coordinate of a point
    equation
    delta
    alpha learning rate    
    steps 
    '''



    #creating a defined domain
    X=np.arange(-4, 4, 0.1)
    Y=np.arange(-4, 4, 0.1)
    X, Y = np.meshgrid (X, Y)


    if equation=='1':
            
        Z=X**2+Y**2            
                
    elif equation=='2':
                
        Z= (-1)*(np.e)**((-1)*((X-1)**2+Y**2)/(0.3*0.3)) -5*((np.e)**((-16)*((X-2)**2+(Y-2)**2)))

    #components of the gradient of each point
    gradx, grady = np.gradient (Z, 0.1, 0.1)
    
    #new place of my descent
    NewX=Xo
    NewY=Yo
    #creating lists to keep my points on the descent
    ListX=[]
    ListY=[]


    #the descent
    for i in range(steps):

        gradxConvert=gradx[int((NewX+4)*10)][int((NewY+4)*10)]
        gradyConvert=grady[int((NewX+4)*10)][int((NewY+4)*10)]


        #gradiant component norm
        norm_grad=(gradxConvert**2 + gradyConvert**2)**0.5

        componentx=delta*(gradxConvert/norm_grad)
        componenty=delta*(gradyConvert/norm_grad)

        NewX=NewY+componentx
        NewY=NewY+componenty
        NewX=round(NewX, 2)
        NewY=round(NewY, 2)

        ListX.append(NewX)
        ListY.append(NewY)

        #∆ to adapt during the descent
        delta=delta*alpha

    
    NewPoints=[ListX, ListY]
    
    #get the minimum values of the points
    recordMinimum=[]
    for i in range(len(ListX)):
        countX=ListX[i]
        county=ListY[i]
        if equation=='1':
            
            Z=countX**2+county**2            
                
        elif equation=='2':
                
            Z= (-1)*(np.e)**((-1)*((countX-1)**2+county**2)/(0.3*0.3)) -5*((np.e)**((-16)*((countX-2)**2+(county-2)**2)))
        
        recordMinimum.append(Z)


    return NewPoints, recordMinimum



'''
equation='1'
steps=200
delta=-0.4
alpha=0.85
Xo=-2
Yo=-2
'''


